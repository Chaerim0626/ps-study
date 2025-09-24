-- 코드를 작성해주세요

SELECT b.ID, (
    SELECT COUNT(*)
    FROM ECOLI_DATA as a
    WHERE a.PARENT_ID = b.ID
) as CHILD_COUNT
FROM ECOLI_DATA as b
ORDER BY b.id