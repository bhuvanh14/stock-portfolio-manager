from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_stocks():
    return {"message": "List of stocks"}

# Example of POST endpoint
# @router.post("/")
# def create_stock(stock: StockSchema):
#     ...
