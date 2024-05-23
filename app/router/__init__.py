from . import entity_extractor, summary_extractor, classify, models_compare

# 定义路由列表
RegisterRouterList = [
    entity_extractor,
    summary_extractor,
    classify,
    models_compare
]
