WITH developer_skills AS (
    SELECT a.ID, GROUP_CONCAT(b.NAME) as total_skill, GROUP_CONCAT(DISTINCT b.CATEGORY) as total_category 
    FROM DEVELOPERS a JOIN SKILLCODES b ON (a.SKILL_CODE & b.CODE) > 0
    GROUP BY a.ID
)
SELECT c.ID, d.EMAIL, d.FIRST_NAME, d.LAST_NAME
FROM developer_skills c JOIN DEVELOPERS d ON c.ID = d.ID
WHERE total_category LIKE '%Front End%'
ORDER BY c.ID