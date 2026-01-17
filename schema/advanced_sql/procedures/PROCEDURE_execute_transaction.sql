CREATE PROCEDURE execute_transaction(
    IN p_portfolio_id INT,
    IN p_stock_id INT,
    IN p_type ENUM('BUY','SELL'),
    IN p_qty INT,
    IN p_price DECIMAL(10,2)
)
BEGIN
    INSERT INTO Transactions(portfolio_id, stock_id, transaction_type, quantity, price)
    VALUES (p_portfolio_id, p_stock_id, p_type, p_qty, p_price);
END;
