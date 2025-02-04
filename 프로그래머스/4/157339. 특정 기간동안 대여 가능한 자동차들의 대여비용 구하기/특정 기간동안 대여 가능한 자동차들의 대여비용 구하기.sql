-- 코드를 입력하세요
WITH choice_car_type AS (
    SELECT a.CAR_ID, a.CAR_TYPE, a.DAILY_FEE, b.START_DATE, b.END_DATE
    FROM CAR_RENTAL_COMPANY_CAR a JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY b ON a.CAR_ID = b.CAR_ID
    WHERE a.CAR_TYPE IN ('세단', 'SUV') 
),
rent_november AS (
    SELECT CAR_ID
    FROM choice_car_type
    WHERE (START_DATE <= '2022-11-30' AND END_DATE >= '2022-11-01')
),
available_car AS (
    SELECT CAR_ID, CAR_TYPE, DAILY_FEE
    FROM choice_car_type 
    WHERE CAR_ID NOT IN (SELECT CAR_ID FROM rent_november)
),
price_car AS (
    SELECT c.*,d.DURATION_TYPE, d.DISCOUNT_RATE
    FROM available_car c JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN d ON c.CAR_TYPE = d.CAR_TYPE
    WHERE d.DURATION_TYPE = '30일 이상'
),
cal_car AS (
    SELECT DISTINCT CAR_ID, CAR_TYPE, DAILY_FEE, ROUND((DAILY_FEE * 30 * (1-(DISCOUNT_RATE/100))),0) AS total_fee
    FROM price_car
)
SELECT DISTINCT CAR_ID, CAR_TYPE, total_fee as FEE
FROM cal_car
WHERE 500000 <= total_fee AND 2000000 > total_fee
ORDER BY total_fee DESC, CAR_TYPE, CAR_ID DESC