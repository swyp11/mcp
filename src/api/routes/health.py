"""Health check and database connection test routes"""
from fastapi import APIRouter, HTTPException
from sqlalchemy import text
from src.database import AsyncSessionLocal
from src.config import redis_client

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/")
async def health_check():
    """
    Basic health check endpoint

    Returns:
    - status: API server status
    """
    return {
        "status": "healthy",
        "message": "API is running"
    }


@router.get("/db")
async def database_health():
    """
    Database connection test endpoint

    Tests connections to:
    - MySQL database
    - Redis cache

    Returns detailed connection status for each service
    """
    result = {
        "mysql": {"status": "unknown", "message": ""},
        "redis": {"status": "unknown", "message": ""}
    }

    # Test MySQL connection
    try:
        async with AsyncSessionLocal() as db:
            await db.execute(text("SELECT 1"))
            result["mysql"]["status"] = "connected"
            result["mysql"]["message"] = "MySQL connection successful"
    except Exception as e:
        result["mysql"]["status"] = "failed"
        result["mysql"]["message"] = f"MySQL connection failed: {str(e)}"

    # Test Redis connection
    try:
        await redis_client.set("health_check", {"status": "ok"}, ttl=10)
        value = await redis_client.get("health_check")
        if value and value.get("status") == "ok":
            result["redis"]["status"] = "connected"
            result["redis"]["message"] = "Redis connection successful"
        else:
            result["redis"]["status"] = "failed"
            result["redis"]["message"] = "Redis read/write test failed"
    except Exception as e:
        result["redis"]["status"] = "failed"
        result["redis"]["message"] = f"Redis connection failed: {str(e)}"

    # Determine overall status
    all_connected = all(
        service["status"] == "connected"
        for service in result.values()
    )

    if not all_connected:
        raise HTTPException(status_code=503, detail=result)

    return {
        "status": "healthy",
        "services": result
    }
