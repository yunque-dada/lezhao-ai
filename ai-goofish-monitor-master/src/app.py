"""
新架构的主应用入口
整合所有路由和服务
"""
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse

from src.api.routes import tasks, logs, settings, prompts, results, login_state, websocket, accounts
from src.api.dependencies import set_process_service, set_scheduler_service
from src.services.task_service import TaskService
from src.services.process_service import ProcessService
from src.services.scheduler_service import SchedulerService
from src.infrastructure.persistence.json_task_repository import JsonTaskRepository
import os

# 全局服务实例
process_service = ProcessService()
scheduler_service = SchedulerService(process_service)

# 设置全局 ProcessService 实例供依赖注入使用
set_process_service(process_service)
set_scheduler_service(scheduler_service)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """应用生命周期管理"""
    print("正在启动应用...")

    task_repo = JsonTaskRepository()
    task_service = TaskService(task_repo)
    tasks_list = await task_service.get_all_tasks()

    for task in tasks_list:
        if task.is_running:
            await task_service.update_task_status(task.id, False)

    await scheduler_service.reload_jobs(tasks_list)
    scheduler_service.start()

    print("应用启动完成")

    yield

    print("正在关闭应用...")
    scheduler_service.stop()
    await process_service.stop_all()
    print("应用已关闭")


# 创建 FastAPI 应用
app = FastAPI(
    title="闲鱼智能监控机器人",
    description="基于AI的闲鱼商品监控系统",
    version="2.0.0",
    lifespan=lifespan
)

# 注册路由
app.include_router(tasks.router)
app.include_router(logs.router)
app.include_router(settings.router)
app.include_router(prompts.router)
app.include_router(results.router)
app.include_router(login_state.router)
app.include_router(websocket.router)
app.include_router(accounts.router)

# 挂载静态文件
app.mount("/static", StaticFiles(directory="static"), name="static")

# 挂载 Vue 3 前端构建产物
if os.path.exists("dist/assets"):
    app.mount("/assets", StaticFiles(directory="dist/assets"), name="assets")

# 健康检查端点
@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "服务正常运行"}


# 认证状态检查端点
from fastapi import HTTPException
from pydantic import BaseModel
from src.infrastructure.config.settings import settings

class LoginRequest(BaseModel):
    username: str
    password: str


@app.post("/auth/status")
async def auth_status(payload: LoginRequest):
    if payload.username == settings.web_username and payload.password == settings.web_password:
        return {"authenticated": True, "username": payload.username}
    raise HTTPException(status_code=401, detail="认证失败")


# 主页路由 - 服务 Vue 3 SPA
@app.get("/")
async def read_root():
    # 读取 index.html 并修改资源路径
    if os.path.exists("dist/index.html"):
        with open("dist/index.html", "r", encoding="utf-8") as f:
            content = f.read()
        # 替换 /assets/ 为 /static/assets/
        content = content.replace('/assets/', '/static/assets/')
        content = content.replace('/vite.svg', '/static/vite.svg')
        return HTMLResponse(content)
    return JSONResponse(
        status_code=500,
        content={"error": "前端构建产物不存在，请先运行 cd web-ui && npm run build"}
    )


# Vue Router 的 fallback 路由 (非静态资源的路径)
@app.get("/{path:path}")
async def serve_vue(path: str):
    """Vue Router fallback - 非 API 路径都返回 index.html"""
    # 排除静态资源和API
    if any(path.startswith(p) for p in ['assets/', 'static/', 'api/']):
        return JSONResponse(status_code=404, content={"error": "Not found"})
    
    if os.path.exists("dist/index.html"):
        return FileResponse("dist/index.html")
    return JSONResponse(status_code=500, content={"error": "前端未构建"})


if __name__ == "__main__":
    import uvicorn
    from src.infrastructure.config.settings import settings
    print(f"启动新架构应用，端口: {settings.server_port}")
    uvicorn.run(app, host="0.0.0.0", port=settings.server_port)
