from fastapi import FastAPI
from routers import users, stocks, portfolios, transactions, watchlist, alerts

app = FastAPI(title="Stock Portfolio Manager")

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(stocks.router, prefix="/stocks", tags=["Stocks"])
app.include_router(portfolios.router, prefix="/portfolios", tags=["Portfolios"])
app.include_router(transactions.router, prefix="/transactions", tags=["Transactions"])
app.include_router(watchlist.router, prefix="/watchlist", tags=["Watchlist"])
app.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])
