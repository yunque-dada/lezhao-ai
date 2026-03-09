@echo off
cd /d "%~dp0"
echo 启动闲鱼监控Web界面...
echo 请访问: http://localhost:9000
python -m http.server 9000
pause
