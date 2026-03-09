import os
import sys

# 设置 Chromium 路径
os.environ['PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH'] = r'D:\快速访问\下载\chromium64_104370\chrome-win\chrome.exe'

# 打印环境变量确认
print('Chromium 路径:', os.environ.get('PLAYWRIGHT_CHROMIUM_EXECUTABLE_PATH'))

# 导入并运行
sys.path.insert(0, '.')
from src.config import load_dotenv
load_dotenv()

print('尝试启动...')
