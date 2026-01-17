from fastapi import APIRouter, HTTPException
import mysql.connector
from ..database import get_connection

router = APIRouter(
    prefix="/portfolios",
    tags=["Portfolios"]
)

# GET all portfolios
@router.get("/")
def get_portfolios():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Portfolios")
    portfolios = cursor.fetchall()
    cursor.close()
    conn.close()
    return portfolios

# GET a specific portfolio
@router.get("/{portfolio_id}")
def get_portfolio(portfolio_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Portfolios WHERE portfolio_id=%s", (portfolio_id,))
    portfolio = cursor.fetchone()
    cursor.close()
    conn.close()
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return portfolio

# CREATE a new portfolio
@router.post("/")
def create_portfolio(user_id: int, name: str):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Portfolios (user_id, name) VALUES (%s, %s)",
            (user_id, name)
        )
        conn.commit()
        portfolio_id = cursor.lastrowid
    except mysql.connector.Error as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Portfolio created", "portfolio_id": portfolio_id}

# UPDATE a portfolio
@router.put("/{portfolio_id}")
def update_portfolio(portfolio_id: int, name: str = None, user_id: int = None):
    conn = get_connection()
    cursor = conn.cursor()
    updates = []
    params = []

    if name:
        updates.append("name=%s")
        params.append(name)
    if user_id:
        updates.append("user_id=%s")
        params.append(user_id)

    if not updates:
        raise HTTPException(status_code=400, detail="No fields to update")

    params.append(portfolio_id)
    query = f"UPDATE Portfolios SET {', '.join(updates)} WHERE portfolio_id=%s"

    try:
        cursor.execute(query, tuple(params))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Portfolio not found")
    except mysql.connector.Error as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Portfolio updated"}

# DELETE a portfolio
@router.delete("/{portfolio_id}")
def delete_portfolio(portfolio_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Portfolios WHERE portfolio_id=%s", (portfolio_id,))
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Portfolio not found")
    except mysql.connector.Error as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"message": "Portfolio deleted"}
