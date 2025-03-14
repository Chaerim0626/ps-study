import sys, copy
input = sys.stdin.readline 
from collections import deque 
from itertools import combinations

def isvalid(x,y):
    return 0 <= x < n and 0 <= y < m
    
def bfs(arr,dq):
    visited = [[0]*m for _ in range(n)]
    dir = [(0,1), (0,-1), (1,0), (-1,0)]

    while dq:
        cx,cy = dq.popleft()
        
        for dx,dy in dir:
            nx,ny = cx+dx, cy+dy

            if isvalid(nx,ny) and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    visited[nx][ny] = 1
                    dq.append((nx,ny))

    count_zero = sum(row.count(0) for row in arr)
    return count_zero
                    
n,m = map(int,input().split())
graph = []
walls = []
virus = []
dq = deque()
result = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            walls.append((i,j))
        elif graph[i][j] == 2:
            virus.append((i,j))
for i,j in virus:
    dq.append((i,j))

for wall in combinations(walls,3):
    tmp_graph = copy.deepcopy(graph)
    
    for i,j in wall:
        tmp_graph[i][j] = 1
        
    dq = deque(virus)
    cnt = bfs(tmp_graph,dq)
    result = max(result,cnt)
    
    for i,j in wall:
        tmp_graph[i][j] = 0
    
print(result)