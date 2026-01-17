CREATE TRIGGER update_current_stock_price
AFTER INSERT ON Stock_Prices
FOR EACH ROW
BEGIN
    UPDATE Stocks
    SET current_price = NEW.price
    WHERE stock_id = NEW.stock_id;
END;
