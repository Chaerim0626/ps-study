
-- 식품 분류별로 가격이 제일 비싼
-- 분류 가격 이름 조회
-- 분류가 과자, 국, 김치, 식용유
-- 식품 가격 기준 내림차순

WITH tmp AS (
    SELECT CATEGORY, MAX(PRICE) as MAX_PRICE
    FROM FOOD_PRODUCT
    WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
    GROUP BY CATEGORY
)

SELECT t.CATEGORY, t.MAX_PRICE, f.PRODUCT_NAME
FROM tmp as t, food_product as f
WHERE t.MAX_PRICE = f.PRICE and t.CATEGORY = f.CATEGORY
ORDER BY MAX_PRICE DESC;