from fastapi import APIRouter
from db.redis.storage import RedisStorage

router = APIRouter()
redis = RedisStorage()

@router.get("")
async def get_items():
    redis.setValue('t','redis test text')
    return [{'foo':redis.getValue('t')}, {'foo2':'bar2'}]

@router.get("/{id}")
async def get_item_by_id(id: int):
    return {'id':id}

@router.put("/{id}")
async def update_item_by_id(id: int):
    return {'id':id}