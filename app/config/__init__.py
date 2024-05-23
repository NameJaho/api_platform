from functools import lru_cache
from dotenv import load_dotenv
from .app_config import *


# 相当于是缓存了函数结果，当相同入参请求时，返回的是缓存结果，不相同时则会重新计算结果,以下是官方给的代码示例和配套讲解图
# https://fastapi.tiangolo.com/zh/advanced/settings/#lru_cache

@lru_cache
def init_config() -> AppConfigSettings:
    # 加载 .env 文件，dotenv_path 变量默认是.env
    load_dotenv()
    # 实例化配置模型
    return AppConfigSettings()


# 获取配置
appSettings = init_config()
