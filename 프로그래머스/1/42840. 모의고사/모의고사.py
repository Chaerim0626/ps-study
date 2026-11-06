def solution(answers):
    n = len(answers)
    p1 = '12345'* 9999 
    p2 = '21232425'*9999
    p3 = '3311224455'*9999
    
    p1 = p1[:n]
    p2 = p2[:n]
    p3 = p3[:n]
    result = ''.join(str(i) for i in answers)
    res = [0,0,0]
    
    for a,b in zip(p1,result):
        if a==b:
            res[0] += 1
    for a,b in zip(p2,result):
        if a==b:
            res[1] += 1
    for a,b in zip(p3,result):
        if a==b:
            res[2] += 1
   
    max_res = max(res) 
    return [i + 1 for i in range(len(res)) if res[i] == max_res]