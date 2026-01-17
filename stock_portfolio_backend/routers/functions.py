from fastapi import APIRouter, HTTPException
import mysql.connector
from ..database import get_connection

router = APIRouter(
    prefix="/functions",
    tags=["Functions"]
)

# 1) Get average price of a stock in a portfolio
@router.get("/avg-price/{portfolio_id}/{stock_id}")
def avg_price(portfolio_id: int, stock_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT get_avg_price(%s, %s)", (portfolio_id, stock_id))
        result = cursor.fetchone()
        return {"portfolio_id": portfolio_id, "stock_id": stock_id, "avg_price": float(result[0]) if result else 0}
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


# 2) Check if portfolio has a stock
@router.get("/has-stock/{portfolio_id}/{stock_id}")
def has_stock(portfolio_id: int, stock_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT has_stock(%s, %s)", (portfolio_id, stock_id))
        result = cursor.fetchone()
        return {"portfolio_id": portfolio_id, "stock_id": stock_id, "has_stock": bool(result[0]) if result else False}
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


# 3) Get total shares in a portfolio
@router.get("/total-shares/{portfolio_id}")
def total_shares(portfolio_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT total_shares(%s)", (portfolio_id,))
        result = cursor.fetchone()
        return {"portfolio_id": portfolio_id, "total_shares": int(result[0]) if result else 0}
    except mysql.connector.Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
