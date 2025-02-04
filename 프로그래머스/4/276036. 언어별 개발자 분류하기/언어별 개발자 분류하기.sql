-- 코드를 작성해주세요
WITH developers_skill AS (
    SELECT a.ID, a.EMAIL, GROUP_CONCAT(DISTINCT b.CATEGORY) as categories, GROUP_CONCAT(b.NAME) as skills
    FROM DEVELOPERS a JOIN SKILLCODES b ON (a.SKILL_CODE & b.CODE) > 0
    GROUP BY a.ID, a.EMAIL
    ORDER BY a.ID, a.EMAIL
), 
last_table AS (
    SELECT 
        CASE
            WHEN categories LIKE '%Front End%' AND skills LIKE '%Python%' THEN 'A'
            WHEN skills LIKE '%C#%' THEN 'B'
            WHEN categories LIKE '%Front End%' THEN 'C'
            END as GRADE,
            ID, EMAIL
    FROM developers_skill
    ORDER BY GRADE, ID
)
SELECT *
FROM last_table
WHERE GRADE IS NOT NULL