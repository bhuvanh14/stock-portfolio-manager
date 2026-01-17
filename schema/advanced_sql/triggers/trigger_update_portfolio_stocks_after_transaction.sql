CREATE TRIGGER update_portfolio_stocks_after_transaction
AFTER INSERT ON Transactions
FOR EACH ROW
BEGIN
    DECLARE existing_qty INT DEFAULT 0;
    DECLARE existing_avg DECIMAL(10,2) DEFAULT 0.00;

    -- Handler for when no row exists yet
    DECLARE CONTINUE HANDLER FOR NOT FOUND
    BEGIN
        SET existing_qty = 0;
        SET existing_avg = 0.00;
    END;

    -- Check if the stock already exists in the portfolio
    SELECT quantity, avg_price
    INTO existing_qty, existing_avg
    FROM Portfolio_Stocks
    WHERE portfolio_id = NEW.portfolio_id
      AND stock_id = NEW.stock_id
    LIMIT 1;

    -- If BUY transaction
    IF NEW.transaction_type = 'BUY' THEN
        IF existing_qty > 0 THEN
            UPDATE Portfolio_Stocks
            SET
                quantity = existing_qty + NEW.quantity,
                avg_price = ((existing_qty * existing_avg) + (NEW.quantity * NEW.price)) / (existing_qty + NEW.quantity)
            WHERE portfolio_id = NEW.portfolio_id
              AND stock_id = NEW.stock_id;
        ELSE
            INSERT INTO Portfolio_Stocks (portfolio_id, stock_id, quantity, avg_price)
            VALUES (NEW.portfolio_id, NEW.stock_id, NEW.quantity, NEW.price);
        END IF;

    -- If SELL transaction
    ELSEIF NEW.transaction_type = 'SELL' THEN
        IF existing_qty >= NEW.quantity THEN
            UPDATE Portfolio_Stocks
            SET quantity = existing_qty - NEW.quantity
            WHERE portfolio_id = NEW.portfolio_id
              AND stock_id = NEW.stock_id;

            -- Remove row if quantity becomes 0
            DELETE FROM Portfolio_Stocks
            WHERE portfolio_id = NEW.portfolio_id
              AND stock_id = NEW.stock_id
              AND quantity = 0;
        ELSE
            -- Prevent selling more than owned
            SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Insufficient quantity to sell';
        END IF;
    END IF;
END;
