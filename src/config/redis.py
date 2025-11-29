# Redis disabled - not used in deployment
# import redis.asyncio as redis
# from typing import Optional
# import json
# from src.config.settings import settings


class RedisClient:
    """Redis cache client (disabled)"""

    def __init__(self):
        self.client = None

    async def connect(self):
        """Connect to Redis (disabled)"""
        pass

    async def disconnect(self):
        """Disconnect from Redis (disabled)"""
        pass

    async def get(self, key: str):
        """Get value from cache (disabled)"""
        return None

    async def set(self, key: str, value: dict, ttl: int = None):
        """Set value in cache (disabled)"""
        pass

    async def delete(self, key: str):
        """Delete key from cache (disabled)"""
        pass

    async def exists(self, key: str) -> bool:
        """Check if key exists (disabled)"""
        return False


# Global Redis client instance (no-op)
redis_client = RedisClient()
