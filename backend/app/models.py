from sqlalchemy import Column, Integer, String, DECIMAL, ForeignKey, Boolean, Enum, TIMESTAMP, DateTime, Date
from sqlalchemy.orm import relationship
from database import Base
import enum

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    created_at = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")
    settings = relationship("Settings", back_populates="user")
    portfolios = relationship("Portfolio", back_populates="user")

class Stock(Base):
    __tablename__ = "stocks"
    stock_id = Column(Integer, primary_key=True)
    symbol = Column(String(10), unique=True, nullable=False)
    company_name = Column(String(100), nullable=False)
    current_price = Column(DECIMAL(10,2))

class Portfolio(Base):
    __tablename__ = "portfolios"
    portfolio_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    name = Column(String(100))
    user = relationship("User", back_populates="portfolios")

class PortfolioStock(Base):
    __tablename__ = "portfolio_stocks"
    portfolio_id = Column(Integer, ForeignKey("portfolios.portfolio_id"), primary_key=True)
    stock_id = Column(Integer, ForeignKey("stocks.stock_id"), primary_key=True)
    quantity = Column(Integer)
    avg_price = Column(DECIMAL(10,2))

class TransactionType(str, enum.Enum):
    BUY = "BUY"
    SELL = "SELL"

class Transaction(Base):
    __tablename__ = "transactions"
    transaction_id = Column(Integer, primary_key=True)
    portfolio_id = Column(Integer, ForeignKey("portfolios.portfolio_id"))
    stock_id = Column(Integer, ForeignKey("stocks.stock_id"))
    transaction_type = Column(Enum(TransactionType))
    quantity = Column(Integer)
    price = Column(DECIMAL(10,2))
    transaction_time = Column(TIMESTAMP, server_default="CURRENT_TIMESTAMP")

class Watchlist(Base):
    __tablename__ = "watchlist"
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    stock_id = Column(Integer, ForeignKey("stocks.stock_id"), primary_key=True)

class AlertType(str, enum.Enum):
    ABOVE = "ABOVE"
    BELOW = "BELOW"

class Alert(Base):
    __tablename__ = "alerts"
    alert_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))
    stock_id = Column(Integer, ForeignKey("stocks.stock_id"))
    target_price = Column(DECIMAL(10,2))
    alert_type = Column(Enum(AlertType))
    active = Column(Boolean, default=True)

class Settings(Base):
    __tablename__ = "settings"
    user_id = Column(Integer, ForeignKey("users.user_id"), primary_key=True)
    email_notifications = Column(Boolean, default=True)
    sms_notifications = Column(Boolean, default=False)
    user = relationship("User", back_populates="settings")
