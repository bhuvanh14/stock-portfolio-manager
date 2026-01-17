import pymysql
from fastapi import Depends

# MySQL connection parameters
DB_HOST = "localhost"
DB_USER = "root"       # replace with your MySQL username
DB_PASSWORD = "41202"   # replace with your MySQL password
DB_NAME = "stock_portfolio_db"

def get_connection():
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        yield conn
    finally:
        conn.close()
