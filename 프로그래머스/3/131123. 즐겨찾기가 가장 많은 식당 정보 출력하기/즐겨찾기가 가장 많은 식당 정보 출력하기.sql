-- 음식종류별로 즐겨찾기 수가 가장 많은
-- 종류,ID,식당이름,즐겨찾기수

SELECT r.FOOD_TYPE, r.REST_ID, r.REST_NAME, r.FAVORITES
FROM REST_INFO r
WHERE (r.FAVORITES, r.FOOD_TYPE) IN (SELECT MAX(r2.FAVORITES), r2.FOOD_TYPE
                     FROM REST_INFO r2 
                     GROUP BY r2.FOOD_TYPE)
ORDER BY FOOD_TYPE DESC;