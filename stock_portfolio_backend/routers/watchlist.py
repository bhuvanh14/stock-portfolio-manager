from fastapi import APIRouter, HTTPException
from ..database import get_connection

router = APIRouter(prefix="/watchlist", tags=["Watchlist"])

# ADD to Watchlist
@router.post("/")
def add_to_watchlist(user_id: int, stock_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Watchlist (user_id, stock_id) VALUES (%s, %s)",
            (user_id, stock_id)
        )
        conn.commit()
        return {"status": "Stock added to watchlist"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# GET Watchlist for a user
@router.get("/{user_id}")
def get_watchlist(user_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Watchlist WHERE user_id=%s", (user_id,))
    watchlist = cursor.fetchall()
    cursor.close()
    conn.close()
    return watchlist

# REMOVE from Watchlist
@router.delete("/{user_id}/{stock_id}")
def remove_from_watchlist(user_id: int, stock_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Watchlist WHERE user_id=%s AND stock_id=%s", (user_id, stock_id))
        conn.commit()
        return {"status": "Stock removed from watchlist"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
