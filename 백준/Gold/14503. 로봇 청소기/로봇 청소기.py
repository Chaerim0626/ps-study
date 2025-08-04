import sys 
input = sys.stdin.readline 
from collections import deque 

n,m = map(int,input().split())
r,c,d = map(int,input().split())

graph = []
for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

# 0 빈칸, 1 벽 
# d 0 북 1 동 2 남 3 서  - 시계방향

def isvalid(x,y):
    return 0 <= x < n and 0 <= y < m
    
def bfs(sx,sy,d):
    dq = deque([(sx,sy,d)])
    cleaned = [[0] * m for _ in range(n)]
    cleaned[sx][sy] = 1
    
    dir = {0:(-1,0), 1: (0,1), 2:(1,0), 3: (0,-1)}
    cnt = 1
    
    while dq:
        cx,cy,d = dq.popleft()

        for i in range(1,5):
            nd = (d-i) % 4  # 90도 회전     
            nx,ny = cx+dir[nd][0], cy+dir[nd][1] # 주변 4칸 확인
        
            if isvalid(nx,ny) and not graph[nx][ny]: # 3. 청소되지 않은 빈칸이 있는 경우
                if not cleaned[nx][ny]:
                    cleaned[nx][ny] = 1
                    cnt += 1
                    dq.append((nx,ny,nd))
                    break 

        else: # 2. 청소되지 않은 빈칸이 없는 경우
            nx,ny = cx+dir[(d+2)%4][0], cy+dir[(d+2)%4][1]

            if not graph[nx][ny]: # 2-1 후진할 수 있다면
                dq.append((nx,ny,d))
                    
            else:  # 후진 할수 없음
                return cnt

    return cnt
        

print(bfs(r,c,d))
            
            
        