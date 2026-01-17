from fastapi import APIRouter, HTTPException
from ..database import get_connection

router = APIRouter(prefix="/stocks", tags=["Stocks"])

# GET all stocks
@router.get("/")
def get_stocks():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Stocks")
    stocks = cursor.fetchall()
    cursor.close()
    conn.close()
    return stocks

# GET stock by ID
@router.get("/{stock_id}")
def get_stock(stock_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Stocks WHERE stock_id=%s", (stock_id,))
    stock = cursor.fetchone()
    cursor.close()
    conn.close()
    if stock:
        return stock
    raise HTTPException(status_code=404, detail="Stock not found")

# CREATE a new stock
@router.post("/")
def create_stock(symbol: str, company_name: str, current_price: float):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Stocks (symbol, company_name, current_price) VALUES (%s, %s, %s)",
            (symbol, company_name, current_price)
        )
        conn.commit()
        stock_id = cursor.lastrowid
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"status": "success", "stock_id": stock_id}

# UPDATE stock price and trigger alerts
@router.put("/update-price/{stock_id}")
def update_stock_price(stock_id: int, current_price: float):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Call the procedure
        cursor.callproc("insert_stock_price", [stock_id, current_price])
        conn.commit()

        # Fetch alerts from procedure
        alerts = []
        for result in cursor.stored_results():
            alerts.extend([r[0] for r in result.fetchall()])

    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()

    return {"status": "success", "alerts": alerts}

# DELETE a stock
@router.delete("/{stock_id}")
def delete_stock(stock_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Stocks WHERE stock_id=%s", (stock_id,))
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
    return {"status": "success"}
