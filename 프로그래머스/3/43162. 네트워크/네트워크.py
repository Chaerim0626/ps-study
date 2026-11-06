def solution(n, computers):
    answer = 0
    visited = [[False] * n for _ in range(n)]

    def dfs(node):
        for i in range(n):
            if not visited[node][i] and computers[node][i]:
                visited[node][i] = True
                visited[i][node] = True
                dfs(i)
        return 1      
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and computers[i][j]:
                visited[i][j] = True
                visited[j][i] = True
                answer += dfs(i)
                
    return answer