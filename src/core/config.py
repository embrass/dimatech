
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://embrass:StrongPass123@localhost:5432/hello"
    JWT_SECRET: str = "supersecret"
    JWT_ALGORITHM: str = "HS256"
    SECRET_KEY: str = "gfdmhghif38yrf9ew0jkf32"  # для подписи вебхуков

settings = Settings() #alembic revision --autogenerate -m "Initial migration"
