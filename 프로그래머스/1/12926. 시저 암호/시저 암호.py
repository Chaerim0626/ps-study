def solution(s, n):
    answer = ''
    
    # 65 + 26 = 91 
    
    for i in s:
        if i == ' ':
            answer += ' '
            continue 
        if i.islower():
            word = chr(ord(i)+n-26) if ord(i) + n > 122 else chr(ord(i)+n)
        elif i.isupper():
            word = chr(ord(i)+n-26) if ord(i) + n > 90 else chr(ord(i)+n)
        answer += word
    return answer 