def solution(begin, target, words):
    
    # 최소 몇단계 거쳐서 변환하는지 구해야함 
    # 한번에 한개 알파벳 바꾸기 
    
    if target not in words:
        return 0
    
    # 느낌상 백트래킹일 것 같은데 cnt세서 푸는 
    n,m = len(begin), len(words)
    visited = [0] * m
    result = float('inf')
    
    def is_conv(a,b):
        return sum(x != y for x,y in zip(a,b)) == 1 
    
    def backtrack(word, cnt):
        nonlocal result 
        
        if word == target:
            result = min(result, cnt)
            return 
        
        for i, w in enumerate(words):
            if not visited[i] and is_conv(word,w):
                visited[i] = True 
                backtrack(w,cnt+1)
                visited[i] = False 
    
    backtrack(begin,0)

    return result