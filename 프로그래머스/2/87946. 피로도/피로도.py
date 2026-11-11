def solution(k, dungeons):

    n = len(dungeons)
    visited = set()
    max_result = 0
    def backtracking(cnt,piro):
        nonlocal max_result 
        max_result = max(max_result,cnt)
        
        for i in range(n):
            if i not in visited and piro >= dungeons[i][0]:
                visited.add(i)
                backtracking(cnt+1,piro-dungeons[i][1])
                visited.remove(i)
                
    backtracking(0,k)
    return max_result