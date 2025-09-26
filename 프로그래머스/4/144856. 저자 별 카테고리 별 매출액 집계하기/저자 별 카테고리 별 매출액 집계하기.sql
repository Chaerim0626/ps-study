
-- 2022-01 판매데이터
-- 저자별, 카테고리별 매출액 (판매량*판매가)
-- 저자id, 저자명, 카테고리, 매출액 리스트 출력 
-- 저자id asc 카테고리 desc

WITH tmp as (
    SELECT a.AUTHOR_NAME, a.AUTHOR_ID, b.PRICE, b.BOOK_ID, b.CATEGORY
    FROM BOOK as b JOIN AUTHOR as a ON
    a.AUTHOR_ID = b.AUTHOR_ID
)

SELECT t.AUTHOR_ID, t.AUTHOR_NAME, t.CATEGORY, SUM(s.SALES* t.PRICE) as TOTAL_SALES
FROM tmp as t, BOOK_SALES as s
WHERE t.BOOK_ID = s.BOOK_ID and
    s.SALES_DATE LIKE '2022-01%'
GROUP BY AUTHOR_ID, CATEGORY
ORDER BY AUTHOR_ID ASC, CATEGORY DESC;