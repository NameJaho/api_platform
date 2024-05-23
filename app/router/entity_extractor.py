# 导入APIRouter
from fastapi import APIRouter, HTTPException

from tools.utils import get_root_path
from uie.uie_predictor import UIEPredictor
from ..models import UieRequest
from ..models.response import EntityExtractorResponse, get_response

# 实例化APIRouter实例
router = APIRouter(tags=["实体抽取"])

import time

SCHEMA = ['公司', '行业', '产品', '技术', '地区', '人物', '疾病', '日期']
root_path = get_root_path()
# 假设的UIEPredictor初始化（替换成正确的导入和初始化）
ie = UIEPredictor(model='uie-base', schema=SCHEMA, task_path=root_path + '/models/entity_extractor')  # , device='gpu'

from loguru import logger


def convert_entity_format(entities):
    _entities = {}
    for item in entities:
        for key, values in item.items():
            count_dict = {}
            for value in values:
                text = value['text']
                count_dict[text] = count_dict.get(text, 0) + 1
            _entities[key] = count_dict
    return _entities


@router.post("/entity_extractor", response_model=EntityExtractorResponse)
async def extract_info(item: UieRequest):
    try:
        # 调用信息提取逻辑
        logger.info("item.query: {}".format(item.query))
        start = time.time()
        result = convert_entity_format(ie(item.query))
        t = round(time.time() - start, 4)
        logger.info(result)
        logger.info(t)
        return get_response({"entities": result, "time": t})
    except Exception as e:
        # 如果出现任何错误，返回错误信息
        raise HTTPException(status_code=500, detail=str(e))
