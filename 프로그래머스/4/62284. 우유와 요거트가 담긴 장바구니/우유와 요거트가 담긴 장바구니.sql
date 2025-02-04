WITH cart_in_products AS (
    SELECT CART_ID, GROUP_CONCAT(NAME) as in_cart
    FROM CART_PRODUCTS
    GROUP BY CART_ID
)
SELECT CART_ID
FROM cart_in_products
WHERE in_cart LIKE '%Milk%' AND in_cart LIKE '%Yogurt%'
ORDER BY 1