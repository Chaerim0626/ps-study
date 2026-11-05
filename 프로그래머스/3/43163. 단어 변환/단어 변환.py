def solution(begin, target, words):
    def diff_one(a,b):
        cnt = 0
        for x,y in zip(a,b):
            if x != y:
                cnt += 1
        return cnt == 1
    
    result = int(1e9)
    visited = [False] * len(words)
    
    def backtracking(cur,target,cnt):
        nonlocal result 
        if cur == target:
            result = min(result,cnt)
        
        for i in range(len(words)):
            if not visited[i] and diff_one(cur,words[i]):
                visited[i] = True 
                backtracking(words[i],target,cnt+1)
                visited[i] = False
                

    backtracking(begin,target,0)
    
    return result if result < int(1e9) else 0