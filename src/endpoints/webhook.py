import hashlib
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.backend.db import get_session
from src.backend import models
from src.title import schemas
from src.core.config import settings

router = APIRouter(prefix="/webhook", tags=["Webhook"])

@router.post("/")
async def process_webhook(data: schemas.WebhookRequest, db: AsyncSession = Depends(get_session)):
    check_str = f"{data.account_id}{data.amount}{data.transaction_id}{data.user_id}{settings.SECRET_KEY}"
    expected_signature = hashlib.sha256(check_str.encode()).hexdigest()
    if data.signature != expected_signature:
        raise HTTPException(status_code=400, detail="Invalid signature")

    result = await db.execute(select(models.Payment).filter(models.Payment.transaction_id == data.transaction_id))
    if result.scalars().first():
        raise HTTPException(status_code=400, detail="Duplicate transaction")


    account = await db.get(models.Account, data.account_id)
    if not account:
        account = models.Account(id=data.account_id, balance=0, user_id=data.user_id)
        db.add(account)
        await db.commit()
        await db.refresh(account)


    payment = models.Payment(
        transaction_id=data.transaction_id,
        amount=data.amount,
        user_id=data.user_id,
        account_id=account.id,
    )
    db.add(payment)
    account.balance += data.amount
    await db.commit()
    return {"status": "success", "balance": account.balance}
