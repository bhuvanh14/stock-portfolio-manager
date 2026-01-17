from fastapi import APIRouter, HTTPException
from ..database import get_connection

router = APIRouter(prefix="/transactions", tags=["Transactions"])

@router.get("/")
def get_all_transactions():
    """
    Get all transactions in the system
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Transactions")
        transactions = cursor.fetchall()
        return {"transactions": transactions}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


@router.get("/{transaction_id}")
def get_transaction(transaction_id: int):
    """
    Get a specific transaction by ID
    """
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Transactions WHERE transaction_id=%s", (transaction_id,))
        transaction = cursor.fetchone()
        if not transaction:
            raise HTTPException(status_code=404, detail="Transaction not found")
        return transaction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


@router.post("/")
def add_transaction(portfolio_id: int, stock_id: int, transaction_type: str, quantity: int, price: float):
    """
    Add a transaction using the stored procedure 'execute_transaction'
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        # Call your procedure
        cursor.callproc("execute_transaction", (portfolio_id, stock_id, transaction_type, quantity, price))
        conn.commit()
        return {"status": "Transaction executed successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()


@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int):
    """
    Delete a transaction. You can create a stored procedure for this if needed.
    """
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Transactions WHERE transaction_id=%s", (transaction_id,))
        conn.commit()
        return {"status": "Transaction deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
