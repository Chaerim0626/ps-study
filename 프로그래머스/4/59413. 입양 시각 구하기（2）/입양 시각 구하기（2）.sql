-- 빈 시간은 0으로 채워야함 

WITH RECURSIVE tmp AS (
    SELECT 0 AS num
    UNION ALL
    SELECT num+1
    FROM tmp
    WHERE num < 23
)
SELECT tmp.num as HOUR, COALESCE(a.COUNT,0) as COUNT from tmp LEFT JOIN
(
    select HOUR(A.DATETIME) as HOUR,
    COUNT(*) as COUNT
    FROM ANIMAL_OUTS AS A
    GROUP BY HOUR
) AS A
ON tmp.num = A.HOUR
GROUP BY tmp.num
ORDER BY tmp.num ASC;