from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    c = Counter(dict(zip(want,number)))
    
    for i in range(len(discount)-9):
        c2 = Counter(discount[i:i+10])
        if c == c2:
            answer += 1
            
    return answer