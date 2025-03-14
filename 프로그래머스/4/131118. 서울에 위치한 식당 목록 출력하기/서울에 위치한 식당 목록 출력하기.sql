SELECT RI.REST_ID, RI.REST_NAME, RI.FOOD_TYPE, RI.FAVORITES, RI.ADDRESS, ROUND(SUM(REVIEW_SCORE) / COUNT(REVIEW_SCORE) , 2) AS SCORE 
FROM REST_INFO RI JOIN REST_REVIEW RR ON RR.REST_ID = RI.REST_ID AND RI.ADDRESS LIKE ('서울%')
GROUP BY 1
ORDER BY 6 DESC, 4 DESC