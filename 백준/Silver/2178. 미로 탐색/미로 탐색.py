from collections import deque

n,m = map(int,input().split())
graph = []
for _ in range(n):
    s = list(map(int,input()))
    graph.append(s)


visited = [[0] * m for _ in range(n)]

def isvalid(x,y):
    return 0 <= x < n and 0 <= y < m
    
def bfs():
    dq = deque([(0,0,1)])
    visited[0][0] = 1
    dir = [(0,1), (0,-1), (1,0), (-1,0)]
    
    while dq:
        cx,cy,cnt = dq.popleft()
        if cx == n-1 and cy == m-1:
            return cnt
            
        for dx,dy in dir:
            nx,ny = cx+dx, cy+dy
            if isvalid(nx,ny) and not visited[nx][ny]:
                if graph[nx][ny]:
                    dq.append((nx,ny,cnt+1))
                    visited[nx][ny] =1 

print(bfs())
                    
        