import sys, copy
input = sys.stdin.readline 
from collections import deque 
n,m = map(int,input().split())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

result = 0 

dir = [(0,1), (0,-1), (1,0), (-1,0)]

def isvalid(x,y):
    return 0 <= x < n and 0 <= y < m
    
def bfs():
    dq = deque()
    tmp_graph = [row[:] for row in graph]

    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                dq.append((i,j))

    while dq:
        cx,cy = dq.popleft()
        for dx,dy in dir:
            nx,ny = cx+dx, cy+dy 

            if isvalid(nx,ny):
                if not tmp_graph[nx][ny]:
                    tmp_graph[nx][ny] = 2
                    dq.append((nx,ny))

    global result 
    cnt = 0
    for i in range(n):
        cnt += tmp_graph[i].count(0)
    result = max(result,cnt)

def makeWall(cnt):
    if cnt == 3:
        bfs()
        return 
        
    for i in range(n):
        for j in range(m):
            if not graph[i][j]:
                graph[i][j] = 1
                makeWall(cnt+1)
                graph[i][j] = 0 # backtracking 

makeWall(0)
print(result)