def solution(s):
    answer = ''
    
    words = s.split(' ')
    
    for word in words:
        for i in range(len(word)):
            if i % 2 == 0:
                answer += word[i].upper()
            elif i % 2 == 1:
                answer += word[i].lower()
        answer += ' '
    
    answer = answer[:-1]
    return answer