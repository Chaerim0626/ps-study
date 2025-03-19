import sys
input = sys.stdin.readline 
from collections import deque 
n,m = map(int,input().split())
graph = []

def isvalid(x,y):
    return 0 <= x < n and 0 <= y < m
    
for _ in range(n):
    nums = list(map(int,input().split()))
    graph.append(nums)
    
def bfs(sx,sy):
    global graph 
    
    visited = [[0]*m for _ in range(n)]
    dq = deque()
    dq.append((sx,sy))
    dir = [(0,1), (0,-1), (1,0), (-1,0)]

    visited[sx][sy] = 1
    
    while dq:
        cx,cy = dq.popleft()

        for dx,dy in dir:
            nx,ny = cx+dx, cy+dy
            if isvalid(nx,ny) and not visited[nx][ny]:
                if cy == sy and cx == sx:
                    if graph[nx][ny]:
                        dq.append((nx,ny))
                        visited[nx][ny] = 1
                        continue 
                elif graph[nx][ny] != 0:
                    graph[nx][ny] = graph[cx][cy] + 1
                    visited[nx][ny] = 1
                    dq.append((nx,ny))

    return graph, visited
            

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            x,y = i,j 
            break 
result, result_v = bfs(x,y)
graph[x][y] = 0

for i in range(n):
    for j in range(m):
        if not result_v[i][j] and graph[i][j]:
            graph[i][j] = -1
            
for row in graph:
    print(*row)
        