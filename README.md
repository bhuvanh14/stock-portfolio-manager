

# Stock Portfolio Management Database

## Abstract

This database is designed to manage users, their stock portfolios, transactions, watchlists, and related stock market information. It supports tracking real-time stock prices, dividend payouts, sector classification, user alerts, and personalized notification settings. The schema ensures data integrity through primary keys, foreign keys, unique constraints, and appropriate data types.

---

## Database Schema Breakdown

### 1. Users

Stores information about users of the system.
Columns:

- user_id INT AUTO_INCREMENT PRIMARY KEY → Unique identifier for each user.
- name VARCHAR(100) NOT NULL → User's name.
- email VARCHAR(100) UNIQUE NOT NULL → User's unique email.
- created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP → Timestamp of user creation.

Constraints:

- Primary Key on user_id.
- Unique constraint on email.

---

### 2. Stocks

Stores details of available stocks.
Columns:

- stock_id INT AUTO_INCREMENT PRIMARY KEY → Unique stock identifier.
- symbol VARCHAR(10) UNIQUE NOT NULL → Stock symbol (e.g., AAPL).
- company_name VARCHAR(100) NOT NULL → Name of the company.
- current_price DECIMAL(10,2) → Current price of the stock.

Constraints:

- Primary Key on stock_id.
- Unique constraint on symbol.

---

### 3. Portfolios

Represents user portfolios.
Columns:

- portfolio_id INT AUTO_INCREMENT PRIMARY KEY → Unique portfolio ID.
- user_id INT → Reference to Users.
- name VARCHAR(100) → Portfolio name.

Constraints:

- Primary Key on portfolio_id.
- Foreign Key user_id references Users(user_id).

---

### 4. Portfolio_Stocks

Tracks the stocks held in each portfolio.
Columns:

- portfolio_id INT → Reference to Portfolios.
- stock_id INT → Reference to Stocks.
- quantity INT → Number of shares.
- avg_price DECIMAL(10,2) → Average purchase price.

Constraints:

- Primary Key on (portfolio_id, stock_id).
- Foreign Keys to Portfolios(portfolio_id) and Stocks(stock_id).

---

### 5. Transactions

Records all buy/sell transactions.
Columns:

- transaction_id INT AUTO_INCREMENT PRIMARY KEY → Unique transaction ID.
- portfolio_id INT → Reference to Portfolios.
- stock_id INT → Reference to Stocks.
- transaction_type ENUM('BUY', 'SELL') → Type of transaction.
- quantity INT → Number of shares.
- price DECIMAL(10,2) → Price per share.
- transaction_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP → Time of transaction.

Constraints:

- Primary Key on transaction_id.
- Foreign Keys to Portfolios(portfolio_id) and Stocks(stock_id).

---

### 6. Stock_Prices

Stores historical stock prices.
Columns:

- stock_id INT → Reference to Stocks.
- price DECIMAL(10,2) → Stock price.
- price_date DATETIME → Timestamp of the price.

Constraints:

- Primary Key on (stock_id, price_date).
- Foreign Key to Stocks(stock_id).

---

### 7. Dividends

Records dividend payouts for stocks.
Columns:

- dividend_id INT AUTO_INCREMENT PRIMARY KEY → Unique dividend ID.
- stock_id INT → Reference to Stocks.
- amount DECIMAL(10,2) → Dividend amount per share.
- dividend_date DATE → Dividend payout date.

Constraints:

- Primary Key on dividend_id.
- Foreign Key to Stocks(stock_id).

---

### 8. Alerts

Tracks user-defined stock price alerts.
Columns:

- alert_id INT AUTO_INCREMENT PRIMARY KEY → Unique alert ID.
- user_id INT → Reference to Users.
- stock_id INT → Reference to Stocks.
- target_price DECIMAL(10,2) → Price that triggers the alert.
- alert_type ENUM('ABOVE', 'BELOW') → Type of alert.
- active BOOLEAN → Whether alert is active.

Constraints:

- Primary Key on alert_id.
- Foreign Keys to Users(user_id) and Stocks(stock_id).

---

### 9. Watchlist

Tracks stocks that a user is watching.
Columns:

- user_id INT → Reference to Users.
- stock_id INT → Reference to Stocks.

Constraints:

- Primary Key on (user_id, stock_id).
- Foreign Keys to Users(user_id) and Stocks(stock_id).

---

### 10. Sectors

Stores stock market sectors.
Columns:

- sector_id INT AUTO_INCREMENT PRIMARY KEY → Unique sector ID.
- name VARCHAR(100) UNIQUE → Sector name (e.g., Technology).

Constraints:

- Primary Key on sector_id.
- Unique constraint on name.

---

### 11. Stock_Sectors

Associates stocks with sectors.
Columns:

- stock_id INT → Reference to Stocks.
- sector_id INT → Reference to Sectors.

Constraints:

- Primary Key on (stock_id, sector_id).
- Foreign Keys to Stocks(stock_id) and Sectors(sector_id).

---

### 12. Settings

Stores user notification preferences.
Columns:

- user_id INT PRIMARY KEY → Reference to Users.
- email_notifications BOOLEAN → Email notification preference.
- sms_notifications BOOLEAN → SMS notification preference.

Constraints:

- Primary Key on user_id.
- Foreign Key to Users(user_id).

---

This schema enforces data integrity, avoids duplication, and supports advanced stock portfolio operations.

---

If you want, I can now create a **clean ER diagram** to visually represent this schema for easier understanding. Do you want me to do that?
