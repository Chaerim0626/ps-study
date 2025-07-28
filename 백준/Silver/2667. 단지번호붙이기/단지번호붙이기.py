from collections import deque

graph = []
n = int(input())
for _ in range(n):
    s = list(map(int,input()))
    graph.append(s)

visited = [[0] * n for _ in range(n)]

def isvalid(x,y):
    return 0 <= x < n and 0 <= y < n
    
def bfs(sx,sy):
    dq = deque([(sx,sy)])
    visited[sx][sy] = 1
    dir = [(0,1), (0,-1), (1,0), (-1,0)]
    cnt = 1
    
    while dq:
        cx,cy = dq.popleft()
            
        for dx,dy in dir:
            nx,ny = cx+dx, cy+dy
            if isvalid(nx,ny) and not visited[nx][ny]:
                if graph[nx][ny]:
                    visited[nx][ny] =1 
                    dq.append((nx,ny))
                    cnt += 1
                    
    return cnt

result = []
for i in range(n):
    for j in range(n):
        if graph[i][j] and not visited[i][j]:
            result.append(bfs(i,j))
            
print(len(result))
result.sort()
for i in result:
    print(i)
    