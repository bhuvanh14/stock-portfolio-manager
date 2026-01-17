from fastapi import APIRouter, HTTPException
from ..database import get_connection

router = APIRouter(prefix="/alerts", tags=["Alerts"])

# CREATE Alert
@router.post("/")
def create_alert(user_id: int, stock_id: int, target_price: float, alert_type: str, active: bool):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO Alerts (user_id, stock_id, target_price, alert_type, active) VALUES (%s, %s, %s, %s, %s)",
            (user_id, stock_id, target_price, alert_type, active)
        )
        conn.commit()
        return {"status": "Alert created successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# READ Alerts for a user
@router.get("/{user_id}")
def get_alerts(user_id: int):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Alerts WHERE user_id=%s", (user_id,))
    alerts = cursor.fetchall()
    cursor.close()
    conn.close()
    return alerts

# UPDATE Alert
@router.put("/{user_id}/{stock_id}")
def update_alert(user_id: int, stock_id: int, target_price: float = None, active: bool = None):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        if target_price is not None:
            cursor.execute("UPDATE Alerts SET target_price=%s WHERE user_id=%s AND stock_id=%s",
                           (target_price, user_id, stock_id))
        if active is not None:
            cursor.execute("UPDATE Alerts SET active=%s WHERE user_id=%s AND stock_id=%s",
                           (active, user_id, stock_id))
        conn.commit()
        return {"status": "Alert updated successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# DELETE Alert
@router.delete("/{user_id}/{stock_id}")
def delete_alert(user_id: int, stock_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("DELETE FROM Alerts WHERE user_id=%s AND stock_id=%s", (user_id, stock_id))
        conn.commit()
        return {"status": "Alert deleted successfully"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()
