from pydantic import BaseModel, Field
from typing import List, Any


def get_response(data: dict = None, code=200):
    """
    统一响应
    """
    return {
        "code": code,
        "data": data
    }


# 通用响应模型
class CommonResponse(BaseModel):
    code: int = Field(..., description="返回信息")
    data: Any  # 可根据需要进一步指定


# 实体抽取响应
class EntityExtractorResponseData(BaseModel):
    entities: dict = Field(..., description="实体字典列表")
    time: float = Field(..., description="响应时间")


class EntityExtractorResponse(CommonResponse):
    data: EntityExtractorResponseData
