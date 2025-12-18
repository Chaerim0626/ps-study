from collections import deque

def solution(prices):
    
    n = len(prices)
    result = [0] * n 
    st = [] # 인덱스
    
    for i, price in enumerate(prices):
        while st and prices[st[-1]] > price:
            j = st.pop()
            result[j] = i-j 
        st.append(i)
    
    while st:
        i = st.pop()
        result[i] = (n-1)-i
    return result