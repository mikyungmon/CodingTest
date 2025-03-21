-- 코드를 작성해주세요
WITH TOTAL_TABLE AS (
    SELECT A.ID,A.PARENT_ID, A.GENOTYPE, B.GENOTYPE AS PARENT_GENOTYPE
    FROM ECOLI_DATA A JOIN ECOLI_DATA B ON A.PARENT_ID = B.ID
    ORDER BY 1
)
SELECT ID, GENOTYPE, PARENT_GENOTYPE
FROM TOTAL_TABLE
WHERE GENOTYPE & PARENT_GENOTYPE = PARENT_GENOTYPE
