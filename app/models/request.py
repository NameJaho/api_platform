from typing import Union
# 导入pydantic对应的模型基类
from pydantic import BaseModel


class BaseRequest(BaseModel):
    """
    请求体参数对应的模型
    """
    pass


class UieRequest(BaseModel):
    """
        请求体参数对应的模型
    """
    query: str
