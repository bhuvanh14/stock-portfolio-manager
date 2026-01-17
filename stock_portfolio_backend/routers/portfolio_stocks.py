from fastapi import APIRouter, HTTPException
from ..database import get_connection

router = APIRouter(prefix="/portfolio-stocks", tags=["Portfolio Stocks"])

@router.get("/{portfolio_id}")
def get_portfolio_stocks(portfolio_id: int):
    """
    Returns the current stocks and quantities for a given portfolio,
    calculated from transactions.
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    try:
        # Aggregate BUY/SELL to get current quantity and average price
        query = """
            SELECT 
                t.stock_id,
                s.symbol,
                s.company_name,
                SUM(CASE WHEN t.transaction_type='BUY' THEN t.quantity
                         WHEN t.transaction_type='SELL' THEN -t.quantity
                         ELSE 0 END) AS quantity,
                CASE WHEN SUM(CASE WHEN t.transaction_type='BUY' THEN t.quantity ELSE 0 END) = 0
                     THEN 0
                     ELSE SUM(CASE WHEN t.transaction_type='BUY' THEN t.quantity * t.price ELSE 0 END) /
                          SUM(CASE WHEN t.transaction_type='BUY' THEN t.quantity ELSE 0 END)
                END AS avg_price
            FROM Transactions t
            JOIN Stocks s ON t.stock_id = s.stock_id
            WHERE t.portfolio_id = %s
            GROUP BY t.stock_id
            HAVING quantity > 0
        """
        cursor.execute(query, (portfolio_id,))
        stocks = cursor.fetchall()
        return {"portfolio_id": portfolio_id, "stocks": stocks}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
