def solution(babbling):
    answer = 0
    
    words = ['aya', 'ye', 'woo', 'ma']
    
    for b in babbling:
        for word in words:
            if word in b:
                b = b.replace(word," ")
                
        b = b.replace(" ","")
    
        if len(b)==0:
            answer += 1
        
    
    return answer