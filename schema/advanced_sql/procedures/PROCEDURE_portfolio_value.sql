CREATE PROCEDURE portfolio_value(
    IN p_portfolio_id INT
)
BEGIN
    SELECT ps.portfolio_id,
           SUM(ps.quantity * s.current_price) AS total_value
    FROM Portfolio_Stocks ps
    JOIN Stocks s ON ps.stock_id = s.stock_id
    WHERE ps.portfolio_id = p_portfolio_id
    GROUP BY ps.portfolio_id;
END;
