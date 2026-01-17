CALL execute_transaction(1,1,'BUY',5,160);


CALL insert_stock_price(1,158);
CALL insert_stock_price(2,2150);
CALL insert_stock_price(3,1850);
CALL insert_stock_price(4,2000);

SELECT get_avg_price(1,1) AS avg_price_aapl_alice;
SELECT has_stock(1,2) AS alice_has_googl;
SELECT has_stock(2,2) AS bob_has_googl;
SELECT total_shares(1) AS total_shares_alice;
SELECT total_shares(2) AS total_shares_bob;

CALL portfolio_value(1);
CALL portfolio_value(2);

SELECT * FROM Portfolio_Stocks;
SELECT * FROM Stock_Prices;
SELECT * FROM Alerts;
SELECT * FROM Stocks;