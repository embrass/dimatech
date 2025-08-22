from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker

from src.core.config import settings
from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(settings.DATABASE_URL, future=True, echo=True)
async_session_maker = async_sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass


async def get_session() -> AsyncSession:
    async with async_session_maker() as session:
        yield session