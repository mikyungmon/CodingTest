-- 코드를 작성해주세요
WITH parent_group AS (
    SELECT PARENT_ID, COUNT(ID) as cnt_child
    FROM ECOLI_DATA
    GROUP BY PARENT_ID 
)
SELECT ed.ID, IFNULL(pg.cnt_child,0) as CHILD_COUNT
FROM ECOLI_DATA ed LEFT JOIN parent_group pg ON ed.ID = pg.PARENT_ID