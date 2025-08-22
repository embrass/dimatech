from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.backend.db import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    full_name = Column(String, nullable=False)
    is_admin = Column(Integer, default=0)

    accounts = relationship("Account", back_populates="user")
    payments = relationship("Payment", back_populates="user")

class Account(Base):
    __tablename__ = "accounts"
    id = Column(Integer, primary_key=True)
    balance = Column(Float, default=0.0)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="accounts")

class Payment(Base):
    __tablename__ = "payments"
    id = Column(Integer, primary_key=True)
    transaction_id = Column(String, unique=True, nullable=False)
    amount = Column(Float, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    account_id = Column(Integer, ForeignKey("accounts.id"))

    user = relationship("User", back_populates="payments")
    account = relationship("Account")