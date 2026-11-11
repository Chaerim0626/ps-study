from collections import deque 

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    result = []
    for i,j in edge:
        graph[i].append(j)
        graph[j].append(i)
        
    def bfs(start,cnt):
        dq = deque([(start,cnt)])
        visited[start] = 1
        
        while dq:
            current,cnt = dq.popleft()
            result.append((current,cnt))      
            for next_node in graph[current]:
                if not visited[next_node]:
                    visited[next_node] = 1
                    dq.append((next_node,cnt+1))
        
    bfs(1,0)
    result.sort(key=lambda x:x[1], reverse=True)
    max_result = result[0][1]
    
    for i,j in result:
        if j == max_result:
            answer += 1
            
    return answer