from collections import deque 
import sys 
input = sys.stdin.readline 

# cnt = 1에서 시작 
n,m = map(int,input().split())
graph = []
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]

def isvalid(x,y):
    return 0 <= x < n and 0 <= y < m
    
for _ in range(n):
    row = list(map(int,input().strip()))
    graph.append(row)

def bfs():
    
    dir = [(0,1), (0,-1), (1,0), (-1,0)]
    visited[0][0][0] =1 
    dq = deque([(0,0,0,1)])

    while dq: 
        cx,cy,wall,cnt = dq.popleft()
        #print(cx,cy,cnt)
        if cx == n-1 and cy == m-1:
            return cnt
            
        for dx,dy in dir:
            nx,ny = dx+cx,dy+cy
            # visited[x][y][0]은 방문 여부, visited[x][y][1]은 부숨 여부 
            if isvalid(nx,ny) and not visited[nx][ny][wall]:
                if graph[nx][ny] == 0:
                    visited[nx][ny][wall] = 1
                    dq.append((nx,ny,wall,cnt+1))

                    if visited[cx][cy][1] == 1:
                        visited[nx][ny][1] = 1 
                        
                else: # 못지나갈때
                    if not wall and not visited[nx][ny][1]:
                        visited[nx][ny][1] = 1
                        dq.append((nx,ny,1,cnt+1))
                
    return -1 
# 모든 좌표에 대해 부술지 안부술지 3차원 
# 100,0000 * 2
print(bfs())
    