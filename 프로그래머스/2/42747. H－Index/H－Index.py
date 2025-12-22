def solution(citations): # 인용횟수
    
    # 논문 n편 중, h번 이상 논문이 h편 이상 
    # (n-h)개 나머지 논문이 h번 이하 인용, h의 최댓값이 H-index 

    citations.sort()
    n = len(citations)
    before,after= 0,0
    
    if len(citations) == 1:
        return citations[0]
    result = 0
    for i in range(citations[-1]):
        tmp = 0
        for item in citations:
            if item >= i:
                tmp += 1
        if tmp >= i:
            result = i
     
       
    return result
