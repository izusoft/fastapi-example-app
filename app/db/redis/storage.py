from redis import Redis
from core.config import (
        REDIS_HOST,
        REDIS_PORT,
        REDIS_DB,
    )

redis_client = Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB)

class RedisStorage:
    def __init__(self):
        self.storage = redis_client

    def getValue(self, key: str):
        return self.storage.get(key)

    def setValue(self, key: str, value):
        self.storage.set(key, value)