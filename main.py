import os

import uvicorn
from fastapi import FastAPI
from app.router import RegisterRouterList
from app.config import appSettings

# 实例化
app = FastAPI()
# 加载路由 
for item in RegisterRouterList:
    app.include_router(item.router)

if __name__ == "__main__":
    # uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    host = appSettings.app_host
    port = appSettings.app_port
    os.system(f'uvicorn main:app --host {host} --port {port} --reload')
