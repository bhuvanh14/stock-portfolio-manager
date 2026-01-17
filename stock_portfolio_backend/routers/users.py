from fastapi import APIRouter
from fastapi import HTTPException
from stock_portfolio_backend.database import get_connection

router = APIRouter(prefix="/users", tags=["Users"])

# ✅ CREATE a new user
@router.post("/create")
def create_user(name: str, email: str):
    conn = get_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO Users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        user_id = cursor.lastrowid
        return {"status": "User created", "user_id": user_id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# ✅ READ all users
@router.get("/")
def get_all_users():
    conn = get_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return {"users": users}

# ✅ READ single user by ID
@router.get("/{user_id}")
def get_user(user_id: int):
    conn = get_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Users WHERE user_id=%s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}

# ✅ UPDATE user
@router.put("/update/{user_id}")
def update_user(user_id: int, name: str = None, email: str = None):
    conn = get_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    cursor = conn.cursor()
    updates = []
    params = []
    if name:
        updates.append("name=%s")
        params.append(name)
    if email:
        updates.append("email=%s")
        params.append(email)
    if not updates:
        raise HTTPException(status_code=400, detail="No update parameters provided")
    params.append(user_id)
    sql = f"UPDATE Users SET {', '.join(updates)} WHERE user_id=%s"
    cursor.execute(sql, tuple(params))
    conn.commit()
    cursor.close()
    conn.close()
    return {"status": "User updated"}

# ✅ DELETE user
@router.delete("/delete/{user_id}")
def delete_user(user_id: int):
    conn = get_connection()
    if not conn:
        raise HTTPException(status_code=500, detail="Database connection failed")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Users WHERE user_id=%s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()
    return {"status": "User deleted"}
