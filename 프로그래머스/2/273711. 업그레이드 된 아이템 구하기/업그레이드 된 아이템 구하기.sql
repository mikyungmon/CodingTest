-- 코드를 작성해주세요
SELECT IT.ITEM_ID, II.ITEM_NAME, II.RARITY
FROM ITEM_TREE IT JOIN ITEM_INFO II ON IT.ITEM_ID = II.ITEM_ID
WHERE PARENT_ITEM_ID IN 
(SELECT ITEM_ID
FROM ITEM_INFO
WHERE RARITY = 'RARE')
ORDER BY 1 DESC
