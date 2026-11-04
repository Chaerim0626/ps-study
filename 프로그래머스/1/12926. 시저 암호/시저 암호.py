def solution(s, n):
    answer = ''
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lower = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    
    for i in range(len(s)): 
        if s[i] == ' ':
            answer += ' '
        elif ord(s[i]) >= 65 and ord(s[i]) <= 90: # 대문자 
            answer += upper[upper.index(s[i]) + n]   
        else:
            answer += lower[lower.index(s[i]) + n]    
    return answer