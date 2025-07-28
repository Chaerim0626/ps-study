from collections import deque
import sys
input = sys.stdin.readline 

graph = []
n,m = map(int,input().split())
for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)
    
def isvalid(x,y):
    return 0 <= x < n and 0 <= y < m

def bfs(i,j, graph):
    visited[i][j] = 1
    dq = deque([(i,j)])
    dir = [(0,1), (0,-1), (1,0), (-1,0)]
    new_graph = [[0] * m for _ in range(n)]
    
    while dq: 
        cnt = 0
        cx,cy = dq.popleft()

        for dx,dy in dir:
            nx,ny = dx+cx, dy+cy # 다음 갈 좌표를 정했음 
            
            if isvalid(nx,ny) and not graph[nx][ny]:
                cnt += 1
            elif isvalid(nx,ny) and not visited[nx][ny]:
                if graph[nx][ny]:
                    visited[nx][ny] = 1
                    dq.append((nx,ny))
                    
        new_graph[cx][cy] = max(0,graph[cx][cy] - cnt)
                    
    return new_graph

result = 0
ice = [(i, j) for i in range(n) for j in range(m) if graph[i][j] != 0]
flag = False
while True:

    visited = [[0] * m for _ in range(n)]
    count = 0
    for i,j in ice:
        if graph[i][j] and not visited[i][j]:
            new_graph = bfs(i,j,graph)
            count += 1

            if count > 1:
                flag = True 
                break 
                
    if count == 0:
        print(0)
        exit()
        
    if flag:
        break
        
    graph = new_graph 
    result += 1

print(result)