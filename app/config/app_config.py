from pydantic_settings import BaseSettings


class AppConfigSettings(BaseSettings):
    """应用配置"""
    app_name: str
    app_port: int
    app_host: str
    app_env: str
    app_debug: bool
