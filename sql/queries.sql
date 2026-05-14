SELECT
COUNT(DISTINCT order_id) AS total_orders,
SUM(quantity) AS total_quantity,
SUM(total_price) AS total_sales
FROM analysis_view
