from redis.asyncio import Redis
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend



async def init_cache():
    redis_client = Redis.from_url(
        "redis://redis:6379",
        encoding="utf8",
        decode_responses=True
    )
    FastAPICache.init(RedisBackend(redis_client),prefix="fastapi-cache")
    