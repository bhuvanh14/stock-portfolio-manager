-- ===========================================
-- Master SQL file to run the entire Stock Portfolio DB
-- ===========================================

-- 1️⃣ Create / Use Database
SOURCE schema/create_use.sql;

-- 2️⃣ Create Tables
SOURCE schema/create.sql;

-- 3️⃣ Insert Fake Data
SOURCE schema/insert.sql;

-- 4️⃣ Create Views
SOURCE schema/views.sql;

-- 5️⃣ Create Functions
SOURCE advanced_sql/function.sql;

-- 6️⃣ Create Procedures
SOURCE advanced_sql/procedure.sql;

-- 7️⃣ Create Triggers
SOURCE advanced_sql/trigger.sql;

-- 8️⃣ Optional: Describe Tables (for verification)
SOURCE schema/describe.sql;

-- 9️⃣ Test Queries (optional)
SELECT * FROM Users;
SELECT * FROM Stocks;
SELECT * FROM UserPortfolioSummary;
CALL AddTransaction(1, 2, 120, 560.50, 'BUY');
SELECT * FROM Alerts;
SELECT GetStockAveragePrice(1);
