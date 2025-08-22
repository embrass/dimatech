from fastapi import APIRouter, Depends, HTTPException

from src.api.deps import get_current_user
from src.title import schemas
from src.backend import models


router = APIRouter(prefix="/admins", tags=["Admins"])

def check_admin(user: models.User):
    if not user.is_admin:
        raise HTTPException(status_code=403, detail="Not an admin")

@router.get("/me", response_model=schemas.UserBase)
async def me(user: models.User = Depends(get_current_user)):
    check_admin(user)
    return user
