-- 코드를 입력하세요
WITH july_total_order AS (
    SELECT FLAVOR, SUM(TOTAL_ORDER) AS flavor_total_order
    FROM JULY 
    GROUP BY FLAVOR
), all_order AS (
    SELECT hf.FLAVOR, (hf.TOTAL_ORDER + jto.flavor_total_order) as all_total_order
    FROM FIRST_HALF hf JOIN july_total_order jto ON hf.FLAVOR = jto.FLAVOR
    GROUP BY hf.FLAVOR
)
SELECT FLAVOR
FROM all_order
ORDER BY all_total_order DESC
LIMIT 3