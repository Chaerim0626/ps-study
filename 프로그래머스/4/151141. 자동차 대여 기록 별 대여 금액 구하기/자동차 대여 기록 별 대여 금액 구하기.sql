-- 대여 / 기록 / 할인 정보 
-- 옵션리스트 SPLIT(',') 해줘야함
-- 일단 자동차 종류 트럭 의 대여기록
-- 대여기록 별로 컬럼명 FEE
-- 대여기록 id, 대여 금액리스트 출력
-- 대여 금액 내림차순, 대여 기록 id 내림차순
-- 여기서 대여 일자를 구하자 

WITH value AS (
    SELECT car.daily_fee, car.car_type, his.history_id,
           DATEDIFF(end_date, start_date) + 1 AS period,
    CASE 
      WHEN DATEDIFF(end_date, start_date) + 1 >= 90 THEN '90일 이상'
      WHEN DATEDIFF(end_date, start_date) + 1 >= 30 THEN '30일 이상'
      WHEN DATEDIFF(end_date, start_date) + 1 >= 7 THEN '7일 이상'
      ELSE 'NONE' END AS duration_type
FROM car_rental_company_rental_history AS his
INNER JOIN car_rental_company_car AS car ON car.car_id = his.car_id
WHERE car.car_type = '트럭')   



SELECT value.history_id, 
    ROUND(value.daily_fee * value.period * 
          (100 - IFNULL(plan.discount_rate,0)) / 100) AS FEE
FROM value
LEFT JOIN car_rental_company_discount_plan AS plan 
    ON plan.duration_type = value.duration_type 
    AND plan.car_type = value.car_type
ORDER BY 2 DESC, 1 DESC