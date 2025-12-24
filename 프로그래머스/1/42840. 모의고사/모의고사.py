def solution(answers):
    
    str1 = '12345'
    str2 = '21232425'
    str3 = '3311224455'
    score1 = 0
    score2 = 0
    score3 = 0
    
    for i in range(len(answers)):
        if str(answers[i]) == str1[i%5]:
            score1 += 1
        if str(answers[i]) == str2[i%8]:
            score2 += 1
        if str(answers[i]) == str3[i%10]:
            score3 += 1
    
    res = [score1,score2,score3]
    result = max(res)
    answer = []
    
    for i in range(len(res)):
        if res[i] == result:
            answer.append(i+1)
        
    return answer