-- 코드를 입력하세요
-- 자동차 정보 / 대여 기록 정보 / 할인 정책 정보
-- 할인: 7일이상, 30일이상, 90일이상 .. 


-- 1. 차종이 세단 or suv
-- 2. 2022-11-1 ~ 2022-11-30 대여 가능
-- 3. 30일간 대여 금액이 (할인받아서) 50만원 이상 200만원 미만

-- 4. 대여 금액 내림차순 
-- 5. 자동차 종류 오름차순 -> 자동차 ID 내림차순

SELECT DISTINCT 
    A.CAR_ID, 
    A.CAR_TYPE, 
    CAST(A.DAILY_FEE * (100 - C.DISCOUNT_RATE) / 100 * 30 AS SIGNED) AS FEE
FROM CAR_RENTAL_COMPANY_CAR AS A
JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS C
    ON A.CAR_TYPE = C.CAR_TYPE
WHERE A.CAR_TYPE IN ('SUV', '세단')
  AND C.DURATION_TYPE = '30일 이상'
  AND (A.DAILY_FEE * (100 - C.DISCOUNT_RATE) / 100 * 30) >= 500000
  AND (A.DAILY_FEE * (100 - C.DISCOUNT_RATE) / 100 * 30) < 2000000
  AND A.CAR_ID NOT IN (    
        SELECT CAR_ID
        FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
        WHERE START_DATE <= '2022-11-30'
          AND END_DATE   >= '2022-11-01'
  )
ORDER BY 
    FEE DESC, 
    A.CAR_TYPE ASC, 
    A.CAR_ID DESC;

