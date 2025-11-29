"""
FastAPI Gateway
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from src.database import init_db
from src.config import settings
from src.api.routes import dress_recommend, health, images, venue_recommend

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan events"""
    # Startup
    await init_db()
    # Redis disabled
    # await redis_client.connect()
    print("✅ API Gateway started")

    yield

    # Shutdown
    # Redis disabled
    # await redis_client.disconnect()
    print("👋 API Gateway shutdown")


# FastAPI app
app = FastAPI(
    title="Wedding Recommendation API",
    description="AI-powered wedding dress and venue recommendation service",
    version="4.0.0",
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
app.include_router(dress_recommend.router)
app.include_router(venue_recommend.router)
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
