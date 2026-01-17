CREATE PROCEDURE insert_stock_price(
    IN p_stock_id INT,
    IN p_price DECIMAL(10,2)
)
BEGIN
    

    -- Insert into Stock_Prices with microseconds
    INSERT INTO Stock_Prices (stock_id, price, price_date)
    VALUES (p_stock_id, p_price, CURRENT_TIMESTAMP(6));

    -- Check alerts and print messages
    SELECT CONCAT('ALERT: Stock ', s.symbol, ' (ID=', p_stock_id, ') triggered alert at price ', p_price) AS alert_message
    FROM Stocks s
    JOIN Alerts a ON s.stock_id = a.stock_id
    WHERE s.stock_id = p_stock_id
      AND a.active = 1
      AND (
           (a.alert_type = 'ABOVE' AND p_price >= a.target_price) OR
           (a.alert_type = 'BELOW' AND p_price <= a.target_price)
      );
END;
