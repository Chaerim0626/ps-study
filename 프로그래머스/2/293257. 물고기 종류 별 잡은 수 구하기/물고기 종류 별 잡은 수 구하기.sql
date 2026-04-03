select COUNT(t1.ID) as FISH_COUNT, t2.FISH_NAME
from fish_info as t1 join fish_name_info as t2 on t1.fish_type = t2.fish_type
group by t2.fish_name
order by FISH_COUNT desc;
