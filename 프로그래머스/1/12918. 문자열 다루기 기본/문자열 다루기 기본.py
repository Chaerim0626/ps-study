def solution(s):
    answer = True
    
    length = len(s)
    if length != 4 and length != 6:
        return False 
    
    for i in s:
        if i in '1234567890':
            continue 
        else:
            return False
    return answer