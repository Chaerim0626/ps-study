from collections import deque
def solution(n, computers):
    answer = 0
    visited = [0] * n 
    
    def bfs(sx):
        
        dq = deque([(sx)])
        while dq:
            cx = dq.popleft()
            
            for j in range(n):
                if not visited[j] and computers[j][cx]:
                    dq.append(j)
                    visited[j] = 1
    
    for i in range(n):
        if not visited[i]:
            bfs(i)
            answer += 1
                    
    return answer