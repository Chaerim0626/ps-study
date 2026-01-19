import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
graph = []
visited = [[0] * n for _ in range(n)]

for _ in range(n):
    row = list(map(int,input().rstrip()))
    graph.append(row)

def isvalid(x,y):
    return 0 <= x < n and 0 <= y < n

def bfs(x,y):
    cnt = 1
    dir = [(0,1), (0,-1),(1,0), (-1,0)]
    dq = deque([(x,y)])

    while dq:
        cx,cy = dq.popleft()

        for dx, dy in dir:
            nx,ny = cx+dx, cy+dy

            if isvalid(nx,ny):
                if not visited[nx][ny] and graph[nx][ny]:
                    visited[nx][ny] = 1
                    cnt += 1
                    dq.append((nx,ny))
                    
    return cnt
   
result = []
for i in range(n):
    for j in range(n):
        if not visited[i][j] and graph[i][j]:
            visited[i][j] = 1
            r = bfs(i,j)
            result.append(r)

result.sort()
print(len(result))
for i in result:
    print(i)
           