import sys 
input = sys.stdin.readline 
from collections import deque

n = int(input())
k = int(input())
apples = set()

for _ in range(k):
    r,c = map(int,input().split())
    apples.add((r-1,c-1))
    
l = int(input())
loc = dict()
for _ in range(l):
    x,c = map(str,input().split())
    x = int(x)
    loc[x] = c
    
graph = [[1 if (i,j) in apples else 0 for j in range(n)] for i in range(n)]

# 몸길이를 늘려 머리를 다음칸에 위치 
# 벽이나 자기자신의 몸과 부딪히면 게임이 끝남 
# 이동한 칸에 사과가 있다면, 그 칸에 있던 사과 삭제, 꼬리 이동 x
# 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리 칸 비움 -> 결국 한칸 앞으로 이동하는 것 

def isvalid(x,y):
    return 0 <= x < n and 0 <= y < n

def bfs(sx,sy,loc):
    dq = deque([(sx,sy)])
    cnt,d = 0,0
    
    while dq:
        #print("cnt: ", cnt)

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        if cnt in loc and loc[cnt] =='D': # 오른쪽 90도 회전
            d = (d+1) % 4
        elif cnt in loc and loc[cnt] == 'L':
            d = (d-1) % 4

        nx,ny = dq[-1][0]+ dx[d], dq[-1][1]+dy[d] # 다음 머리 좌표
        
        if isvalid(nx,ny) and (nx,ny) not in dq: # 다음 머리 좌표가 벽이나 자기 몸이 아닐 경우
            if graph[nx][ny]: # 이동한 칸이 사과라면 
                graph[nx][ny] = 0
                dq.append((nx,ny))
                
            else: # 이동한 칸이 사과가 아니라면 
                dq.popleft()
                dq.append((nx,ny))
                    
        elif not isvalid(nx,ny) or (nx,ny) in dq:
            cnt += 1
            return cnt

        cnt += 1


print(bfs(0,0,loc))
                    
                    
                    
                
                
                
            
            
    