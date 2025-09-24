-- 코드를 입력하세요
SELECT MEMBER_ID, MEMBER_NAME, GENDER,
DATE_FORMAT(DATE_OF_BIRTH, '%Y-%m-%d') as DATE_OF_BIRTH
from MEMBER_PROFILE
where gender = 'W' and DATE_OF_BIRTH = DATE_FORMAT(DATE_OF_BIRTH, '%Y-03-%d') and TLNO is not null 
order by member_id asc;
