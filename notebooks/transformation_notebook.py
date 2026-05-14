df = spark.read.format("csv") \
.option("header","true") \
.option("inferSchema","true") \
.load("/mnt/raw/")

df.createOrReplaceTempView("analysis_view")

result = spark.sql("""

SELECT
COUNT(DISTINCT order_id) AS total_orders,
SUM(quantity) AS total_quantity,
SUM(total_price) AS total_sales

FROM analysis_view

""")

display(result)
