def solution(k, dungeons):
    max_result = 0
    n = len(dungeons)
    visited = set()
    
    def backtracking(start,piro):
        nonlocal max_result 
        
        max_result = max(max_result,start)
 
        for i in range(n):
            if i not in visited and piro >= dungeons[i][0]:
                visited.add(i)
                backtracking(start+1,piro-dungeons[i][1])
                visited.remove(i)
                
    backtracking(0,k)
    
    return max_result