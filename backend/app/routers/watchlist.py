from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_watchlist():
    return {"message": "Watchlist endpoint working"}
