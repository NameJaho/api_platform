from typing import Union
# 导入pydantic对应的模型基类
from pydantic import BaseModel


class BaseParams(BaseModel):
    """
    请求体参数对应的模型
    """
    user_name: str
    age: int
    city: Union[str, None]


class UieParams(BaseModel):
    """
        请求体参数对应的模型
    """
    query: str
