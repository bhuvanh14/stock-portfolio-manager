from fastapi import FastAPI
from stock_portfolio_backend.routers import users, stocks, portfolios, transactions, alerts, watchlist, functions

app = FastAPI()

app.include_router(users.router)
app.include_router(stocks.router)
app.include_router(portfolios.router)
app.include_router(transactions.router)
app.include_router(alerts.router)
app.include_router(watchlist.router)
app.include_router(functions.router)



@app.get("/")
def root():
    return {"message": "Hello! Backend is running"}
