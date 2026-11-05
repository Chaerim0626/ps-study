def solution(k, dungeons):
    answer = 0
    visited = set()
    
    def backtracking(piro,cnt):
        nonlocal answer
        
        answer = max(answer,cnt)
        
        for i,(current, p) in enumerate(dungeons):
            if i not in visited:
                visited.add(i)
                if piro >= current: 
                    backtracking(piro-p,cnt+1)
                visited.remove(i)
                
    backtracking(k,0)
        
    return answer