import sys 
input = sys.stdin.readline 
from collections import deque 

n,m = map(int,input().split())
r,c,d = map(int,input().split())
# 방의 크기: n*m 직사각형 
# 좌표 (r,c)로 나타냄 
# 구해야하는 것: 청소하는 칸의 개수 

graph = []
for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

visited = [[0] * m for _ in range(n)] # 이 리스트로 청소 판별

def isvalid(x,y):
    return 0 <= x < n and 0 <= y < m
    
def bfs(r,c,d):

    dq = deque([(r,c,d)])
    dir = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)} # 북동남서 
    cnt = 0
    
    while dq:
        cx,cy,d = dq.popleft()
        flag = False

        if not visited[cx][cy]:

            visited[cx][cy] = 1
            cnt += 1
            
        for i in range(4): # 주변 4칸 확인
            nx,ny = dir[i][0]+cx, dir[i][1]+cy 

            if isvalid(nx,ny) and not visited[nx][ny]:
                if graph[nx][ny] == 0: # 청소안한 빈칸 있는 경우 

                    while True:

                        if d > 0: # 반시계 방향 회전
                            d -= 1
                        else:
                            d = 3
                            
                        nx2,ny2 = dir[d][0]+cx, dir[d][1]+cy # 바라보는 방향 적용
                        if isvalid(nx2,ny2) and not visited[nx2][ny2]:
                            if graph[nx2][ny2] == 0:
                                dq.append((nx2,ny2,d)) # 한 칸 전진
                                flag = True # 1번 돌아가기
                                break 

            if flag:
                break 

        else: 
            nx3,ny3 = cx+dir[(d+2)%4][0], cy+dir[(d+2)%4][1]
            if isvalid(nx3,ny3) and graph[nx3][ny3] == 0: # 후진할 수 있다면
                dq.append((nx3,ny3,d)) # 한 칸 후진 
                flag = True # 1번 돌아가기
                   
            elif not isvalid(nx3,ny3) or graph[nx3][ny3] == 1:
                return cnt


    return cnt 

print(bfs(r,c,d))
                    
            
    