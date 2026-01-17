INSERT IGNORE INTO Users(name,email) VALUES
('Alice','alice@example.com'),
('Bob','bob@example.com'),
('Charlie','charlie@example.com'),
('David','david@example.com'),
('Eve','eve@example.com');

INSERT IGNORE INTO Stocks(symbol, company_name, current_price) VALUES
('AAPL','Apple Inc.',150),
('GOOGL','Alphabet Inc.',2000),
('MSFT','Microsoft Corp.',300),
('AMZN','Amazon.com Inc.',3500),
('TSLA','Tesla Inc.',800);

INSERT IGNORE INTO Portfolios(user_id,name) VALUES
(1,'Alice Tech Portfolio'),
(2,'Bob Growth Portfolio'),
(3,'Charlie Value Portfolio'),
(4,'David Dividend Portfolio'),
(5,'Eve Mixed Portfolio');

INSERT IGNORE INTO Portfolio_Stocks(portfolio_id, stock_id, quantity, avg_price) VALUES
(1,1,10,150),   
(1,2,5,2000),   
(2,2,20,2000),  
(3,3,15,300),   
(4,4,8,3500),   
(5,5,12,800);   

INSERT IGNORE INTO Transactions(portfolio_id, stock_id, transaction_type, quantity, price) VALUES
(1,1,'BUY',10,150),
(1,2,'BUY',5,2000),
(2,2,'BUY',20,2000),
(3,3,'BUY',15,300),
(4,4,'BUY',8,3500),
(5,5,'BUY',12,800);

INSERT IGNORE INTO Stock_Prices(stock_id, price, price_date) VALUES
(1,150,NOW() - INTERVAL 5 DAY),
(1,155,NOW() - INTERVAL 4 DAY),
(2,2000,NOW() - INTERVAL 5 DAY),
(2,2100,NOW() - INTERVAL 4 DAY),
(3,300,NOW() - INTERVAL 5 DAY),
(4,3500,NOW() - INTERVAL 4 DAY),
(5,800,NOW() - INTERVAL 5 DAY);

INSERT IGNORE INTO Dividends(stock_id, amount, dividend_date) VALUES
(1,0.82,'2025-10-01'),
(2,0.0,'2025-10-01'),
(3,0.56,'2025-10-02'),
(4,1.2,'2025-10-03'),
(5,0.0,'2025-10-04');

INSERT IGNORE INTO Alerts(user_id, stock_id, target_price, alert_type, active) VALUES
(2,2,2100,'ABOVE',TRUE),
(2,2,1900,'BELOW',TRUE),
(3,3,310,'ABOVE',TRUE),
(4,4,3600,'ABOVE',TRUE),
(5,5,750,'BELOW',TRUE);

INSERT IGNORE INTO Watchlist(user_id, stock_id) VALUES
(1,2),
(2,1),
(3,4),
(4,5),
(5,3);

INSERT IGNORE INTO Sectors(name) VALUES
('Technology'),
('Finance'),
('Consumer Discretionary'),
('Healthcare'),
('Energy');

INSERT IGNORE INTO Stock_Sectors(stock_id, sector_id) VALUES
(1,1),
(2,1),
(3,1),
(4,3),
(5,1);

INSERT IGNORE INTO Settings(user_id, email_notifications, sms_notifications) VALUES
(1,1,0),
(2,1,0),
(3,1,0),
(4,1,0),
(5,1,0);