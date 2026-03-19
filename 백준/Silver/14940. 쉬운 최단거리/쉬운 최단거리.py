import sys 
input = sys.stdin.readline 
from collections import deque 


n,m = map(int,input().split())
graph = []
visited = [[-1]* m for _ in range(n)]
for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

        
def isvalid(x,y):
    return 0 <= x < n and 0 <= y < m
def bfs(sx,sy):
    dir = [[0,1], [0,-1], [1,0], [-1,0]]
    dq = deque([(sx,sy)])

    visited[sx][sy] = 0

    while dq:
        cx,cy = dq.popleft()

        for dx,dy in dir:
            nx,ny = dx+cx,dy+cy
            if isvalid(nx,ny):
                if visited[nx][ny] == -1 and graph[nx][ny]:
                    dq.append((nx,ny))
                    visited[nx][ny] = visited[cx][cy] + 1

for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            sx,sy = i,j
        elif graph[i][j] == 0:
            visited[i][j] = 0

bfs(sx,sy)
for row in visited:
    print(*row)