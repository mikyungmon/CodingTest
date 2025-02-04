-- 코드를 작성해주세요
WITH row_number_table AS (
    SELECT *, RANK() OVER (ORDER BY SIZE_OF_COLONY DESC) as rn
    FROM ECOLI_DATA
), total_row_table AS (
    SELECT COUNT(*) AS total_row
    FROM ECOLI_DATA
)
SELECT rnt.ID, 
    CASE WHEN (0 < rnt.rn AND trt.total_row * 0.25 >= rnt.rn) THEN 'CRITICAL'
    WHEN (trt.total_row * 0.25 < rnt.rn AND trt.total_row * 0.5 >= rnt.rn) THEN 'HIGH'
    WHEN (trt.total_row * 0.5 < rnt.rn AND trt.total_row * 0.75 >= rnt.rn) THEN 'MEDIUM'
    WHEN (trt.total_row * 0.75 < rnt.rn AND trt.total_row * 1 >= rnt.rn) THEN 'LOW'
    END AS COLONY_NAME
FROM row_number_table rnt CROSS JOIN total_row_table trt 
ORDER BY rnt.ID
# SELECT ID,
#     CASE WHEN (0 < rn AND total_row * 0.25 >= rn) THEN 'CRITICAL'
#     WHEN (total_row * 0.25 < rn AND total_row * 0.5 >= rn) THEN 'HIGH'
#     WHEN (total_row * 0.5 < rn AND total_row * 0.75 >= rn) THEN 'MEDIUM'
#     WHEN (total_row * 0.75 < rn AND total_row * 1 >= rn) THEN 'LOW'
#     END AS COLONY_NAME
# FROM join_tables
# ORDER BY ID