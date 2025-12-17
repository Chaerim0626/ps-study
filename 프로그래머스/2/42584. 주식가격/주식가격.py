from collections import deque

def solution(prices):
    dq = deque(prices)
    result = []
    
    while dq:
        cur_price = dq.popleft()
        time = 0
        
        for i in dq:
            time += 1
            if cur_price > i:
                break 
        result.append(time)
        
    return result