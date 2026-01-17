from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_stocks():
    return {"message": "List of stocks"}
