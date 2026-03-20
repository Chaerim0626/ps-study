import sys 
input = sys.stdin.readline 
from collections import deque 


m,n,k = map(int,input().split()) #  m = x , n = y 
graph = [[0]*n for _ in range(m)]
for _ in range(k):
    x1,y1,x2,y2 = map(int,input().split())
    for i in range(x1,x2):
        for j in range(y1,y2):
            graph[j][i] = 1
#print(graph)    
result = []

def isvalid(x,y):
    return 0 <= x< m and 0 <= y < n

def bfs(x,y):
    global answer 
    dir = [(0,1), (0,-1), (1,0) ,(-1,0)]
    dq = deque([(x,y)])

    graph[x][y] = 1
    size = 1

    while dq:
        cx,cy = dq.popleft()
        for dx,dy in dir:
            nx,ny = cx+dx, cy+dy
            if isvalid(nx,ny):
                if graph[nx][ny] == 0:
                    graph[nx][ny] = 1
                    dq.append((nx,ny))
                    size += 1

    result.append(size)

for i in range(m):
    for j in range(n):
        if not graph[i][j]:
            bfs(i,j)

result.sort()
print(len(result))
print(*result)