from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from src.title import schemas
from src import crud
from src.backend.db import get_session
from src.api.deps import get_current_user
from src.api import auth
from src.backend import models

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/login", response_model=schemas.TokenResponse)
async def login(data: schemas.LoginRequest, db: AsyncSession = Depends(get_session)):
    user = await crud.get_user_by_email(db, data.email)
    if not user or not auth.verify_password(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = auth.create_access_token({"sub": str(user.id)})
    return {"access_token": token}

@router.get("/me", response_model=schemas.UserDetail)
async def get_me(user: models.User = Depends(get_current_user)):
    return user
