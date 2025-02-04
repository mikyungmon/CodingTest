WITH may_food_order AS(
    SELECT PRODUCT_ID, SUM(AMOUNT) AS SUM_COUNT
    FROM FOOD_ORDER
    WHERE LEFT(PRODUCE_DATE,7) = '2022-05'
   GROUP BY 1
)
SELECT mfo.PRODUCT_ID, FOOD_PRODUCT.PRODUCT_NAME, mfo.SUM_COUNT* FOOD_PRODUCT.PRICE AS TOTAL_SALES
FROM may_food_order mfo JOIN FOOD_PRODUCT ON mfo.PRODUCT_ID = FOOD_PRODUCT.PRODUCT_ID
ORDER BY 3 DESC, 1