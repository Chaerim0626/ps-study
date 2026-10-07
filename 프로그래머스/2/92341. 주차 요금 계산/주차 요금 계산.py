import math
from collections import defaultdict 

def solution(fees, records):
    answer = []
    base_time, base_fee, unit_time, unit_fee = fees
    
    def to_min(t):
        h,m = map(int,t.split(':'))
        return h * 60 + m 
    
    in_time = {}
    total = defaultdict(int)
    
    for r in records:
        t, car, kind = r.split()
        if kind == 'IN':
            in_time[car] = t 
            pass
        else: # out 
            total[car] += to_min(t) - to_min(in_time[car])
            del in_time[car]
    
    for car, t in in_time.items():
        total[car] += to_min('23:59') - to_min(t)
        
    # 차량 번호 순서대로 요금 계산
    for car in sorted(total):
        if total[car] <= base_time:
            answer.append(base_fee)
        else:
            answer.append(base_fee + math.ceil((total[car]-base_time)/unit_time)*unit_fee)
    
    return answer