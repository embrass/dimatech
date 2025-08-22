#uvicorn src.main:app --reload
from fastapi import FastAPI
from src.endpoints import users, admins, webhook

app = FastAPI()

app.include_router(users.router)
app.include_router(admins.router)
app.include_router(webhook.router)
