-- 코드를 입력하세요
WITH RENTAL_STATUS AS (
    SELECT *,
     CASE 
        WHEN START_DATE < '2022-10-16' AND END_DATE < '2022-10-16' THEN '대여 가능'
        WHEN START_DATE <= '2022-10-16' OR END_DATE <= '2022-10-16' THEN '대여중' 
        ELSE '대여 가능'
        END AS AVAILABILITY
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
),
CONCAT_AVAIL AS (
    SELECT CAR_ID, GROUP_CONCAT(AVAILABILITY) AS GROUP_AVAIL
    FROM RENTAL_STATUS
    GROUP BY CAR_ID
)
SELECT CAR_ID,
    CASE
        WHEN GROUP_AVAIL LIKE '%대여중%' THEN '대여중'
        ELSE '대여 가능'
    END AS AVAILABILITY
FROM CONCAT_AVAIL
ORDER BY 1 DESC