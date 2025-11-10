from pydantic_settings import BaseSettings
from typing import Optional


class Settings(BaseSettings):
    """Application configuration settings"""

    # OpenAI
    openai_api_key: str

    # MySQL (환경변수: DB_HOST, DB_PORT, DB_USERNAME, DB_PASSWORD, DB_NAME)
    db_host: str = "localhost"
    db_port: int = 3306
    db_username: str = "root"
    db_password: str
    db_name: str = "wedding_dress_db"

    # Redis
    redis_host: str = "localhost"
    redis_port: int = 16379
    redis_password: Optional[str] = None
    redis_db: int = 0

    # Application
    app_host: str = "0.0.0.0"
    app_port: int = 8000
    cache_ttl: int = 3600

    # Image Storage
    image_base_path: str = "/data/images"  # 이미지가 저장된 서버 경로

    @property
    def mysql_url(self) -> str:
        return f"mysql+aiomysql://{self.db_username}:{self.db_password}@{self.db_host}:{self.db_port}/{self.db_name}"

    @property
    def redis_url(self) -> str:
        if self.redis_password:
            return f"redis://:{self.redis_password}@{self.redis_host}:{self.redis_port}/{self.redis_db}"
        return f"redis://{self.redis_host}:{self.redis_port}/{self.redis_db}"

    class Config:
        env_file = ".env-ai"
        case_sensitive = False


settings = Settings()
