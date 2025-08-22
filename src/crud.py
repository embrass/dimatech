from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.backend import models

async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(models.User).filter(models.User.email == email))
    return result.scalars().first()

async def create_user(db: AsyncSession, email: str, password: str, full_name: str, is_admin: int = 0):
    user = models.User(email=email, password=password, full_name=full_name, is_admin=is_admin)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user
