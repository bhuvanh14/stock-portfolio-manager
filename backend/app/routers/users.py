from fastapi import APIRouter, Depends, HTTPException
from database import get_connection
from pydantic import BaseModel

router = APIRouter()

class UserCreate(BaseModel):
    name: str
    email: str

class User(BaseModel):
    user_id: int
    name: str
    email: str

@router.post("/", response_model=User)
def create_user(user: UserCreate, conn=Depends(get_connection)):
    with conn.cursor() as cursor:
        # Check if email exists
        cursor.execute("SELECT * FROM users WHERE email=%s", (user.email,))
        existing = cursor.fetchone()
        if existing:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        # Insert new user
        cursor.execute(
            "INSERT INTO users (name, email) VALUES (%s, %s)", 
            (user.name, user.email)
        )
        conn.commit()
        
        cursor.execute("SELECT * FROM users WHERE email=%s", (user.email,))
        new_user = cursor.fetchone()
    return new_user

@router.get("/", response_model=list[User])
def get_users(conn=Depends(get_connection)):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
    return users
