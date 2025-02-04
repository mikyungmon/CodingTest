WITH MAX_LENGTH AS (
    SELECT A.FISH_NAME, B.LENGTH, B.FISH_TYPE
    FROM FISH_NAME_INFO A JOIN (SELECT MAX(LENGTH) AS LENGTH, FISH_TYPE FROM FISH_INFO GROUP BY FISH_TYPE) B ON A.FISH_TYPE = B.FISH_TYPE
)
SELECT D.ID, C.FISH_NAME, C.LENGTH
FROM MAX_LENGTH C JOIN FISH_INFO D ON C.LENGTH = D.LENGTH AND C.FISH_TYPE = D.FISH_TYPE