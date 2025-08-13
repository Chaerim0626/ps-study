import sys
input = sys.stdin.readline 
from collections import deque

n,l,r = map(int,input().split())
graph = []
for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

result = 0

def isvalid(x,y):
    return 0 <= x < n and 0 <= y < n

def open(x,y):
        
    area = bfs(x,y)
    if len(area) == 1 :
        return area, 0
            
    cnt,tot = 0,0
    
    for x,y in area:
        cnt += 1
        tot += graph[x][y]

    return area, int(tot / cnt)

def cnt(x,y):
    
    area,avg = open(x,y)

    if len(area) == 1:
        return False 
        
    for x, y in area:
        graph[x][y] = avg

    return True
        
def bfs(sx,sy):
    global graph 
    global visited
    visited[sx][sy] = 1
    dir = [(0,1), (0,-1), (1,0), (-1,0)]
    dq = deque([(sx,sy)])
    area = [(sx,sy)]
    
    while dq:
        cx,cy = dq.popleft()
        for dx,dy in dir:
            nx,ny = cx+dx, cy+dy
            
            if isvalid(nx,ny) and not visited[nx][ny]:
                if l <= abs(graph[cx][cy] - graph[nx][ny]) and abs(graph[cx][cy] - graph[nx][ny]) <= r:
                    dq.append((nx,ny))
                    area.append((nx,ny))
                    visited[nx][ny] = 1
                    
    return area
    
result = 0

while True:
    visited = [[0] * n for _ in range(n)]
    flag = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if cnt(i,j):
                    flag = True
    if not flag:
        break
    else:
        result += 1
        
print(result)
    