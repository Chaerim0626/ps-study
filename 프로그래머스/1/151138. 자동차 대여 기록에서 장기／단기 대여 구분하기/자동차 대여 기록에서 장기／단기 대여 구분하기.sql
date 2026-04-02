-- 코드를 입력하세요



select HISTORY_ID, CAR_ID, DATE_FORMAT(START_DATE, '%Y-%m-%d') as START_DATE
, DATE_FORMAT(END_DATE, '%Y-%m-%d') as END_DATE, 
if(datediff(end_date,start_date)+1 >= 30 , '장기 대여' , '단기 대여') as RENT_TYPE
from car_rental_company_rental_history
where START_DATE LIKE '2022-09%'
order by HISTORY_ID DESC;

