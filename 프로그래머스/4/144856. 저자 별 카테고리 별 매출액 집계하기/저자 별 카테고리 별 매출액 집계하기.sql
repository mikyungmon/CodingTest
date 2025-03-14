WITH january_sales AS (
    SELECT *
    FROM BOOK_SALES
    WHERE SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
),
book_cnt AS (
    SELECT BOOK_ID, SUM(SALES) AS cnt_book
    FROM january_sales
    GROUP BY BOOK_ID
),
book_join AS (
    SELECT bc.*, b.CATEGORY, b.AUTHOR_ID, b.PRICE
    FROM book_cnt bc JOIN BOOK b ON bc.BOOK_ID = b.BOOK_ID
),
author_join AS (
    SELECT bj.*, a.AUTHOR_NAME
    FROM book_join bj JOIN AUTHOR a ON bj.AUTHOR_ID = a.AUTHOR_ID
),
category_group AS(
    SELECT AUTHOR_ID, AUTHOR_NAME, CATEGORY, (cnt_book*PRICE) AS TOTAL_SALES
    FROM author_join
)
SELECT AUTHOR_ID, AUTHOR_NAME, CATEGORY, SUM(TOTAL_SALES) AS TOTAL_SALES
FROM category_group
GROUP BY AUTHOR_NAME, CATEGORY
ORDER BY 1 ASC ,3 DESC