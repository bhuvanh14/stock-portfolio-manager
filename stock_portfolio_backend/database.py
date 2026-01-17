import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="41202",  # replace with your MySQL password
            database="stock_portfolio_db"  # your database
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error connecting to MySQL:", e)
        return None
