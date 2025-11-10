"""
FastAPI Gateway
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.database import init_db
from src.config import redis_client, settings
from src.api.routes import recommend, health, images

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    await init_db()
    await redis_client.connect()
    print("✅ API Gateway started")

    yield

    # Shutdown
    await redis_client.disconnect()
    print("👋 API Gateway shutdown")


# FastAPI app
app = FastAPI(
    title="Wedding Dress Recommendation API",
    description="AI-powered wedding dress recommendation service",
    version="3.0.0",
    lifespan=lifespan
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(recommend.router)
app.include_router(health.router)
app.include_router(images.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "src.api.main:app",
        host=settings.app_host,
        port=settings.app_port,
        reload=True
    )
