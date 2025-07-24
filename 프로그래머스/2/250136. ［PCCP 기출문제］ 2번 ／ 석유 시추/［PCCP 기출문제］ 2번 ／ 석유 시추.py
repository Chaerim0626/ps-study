import copy
from collections import deque

def solution(land):
    
    n = len(land)
    m = len(land[0])
    visited = [[0] * m for _ in range(n)]
    sizes = []
    loc = []
    
    def isvalid(x,y):
        return 0 <= x < n and 0 <= y < m 
    
    def bfs(i,j,t):
        dq = deque()
        dq.append((i,j))
        visited[i][j] = 1
        dir = [(0,1), (0,-1), (1,0), (-1,0)]
        
        size = 1
        loc.append((i,j,t))
        
        while dq:
            cx,cy = dq.popleft()
            
            for dx, dy in dir:
                nx,ny = cx+dx, cy+dy 
                
                if isvalid(nx,ny) and land[nx][ny]:
                    if not visited[nx][ny]:
                        dq.append((nx,ny))
                        visited[nx][ny] = 1
                        size += 1
                        loc.append((nx,ny,t))
        return size
    
    t = 1
    for i in range(n):
        for j in range(m):
            if land[i][j] and not visited[i][j]:
                r = bfs(i,j,t)
                sizes.append((t,r))
                t += 1

    for i,j,t in loc:
        visited[i][j] = sizes[t-1][1] 
        
    # 이제 해야할일 : 같은 영역은 set취급하여 열별로 계산 
    
    loc.sort(key=lambda x: x[1])
    
    result = []
    result.append((loc[0][0],loc[0][1],visited[loc[0][0]][loc[0][1]]))

    for i in range(1, len(loc)):
        if loc[i][1] == loc[i-1][1] and loc[i][2] == loc[i-1][2]:
            # 같은 열이고, 같은 그룹이라면
            pass
        else:
            result.append((loc[i][0],loc[i][1],visited[loc[i][0]][loc[i][1]]))
            
    answer = 0
    cur = result[0][2]
    
    for i in range(1,len(result)):
        if result[i-1][1] == result[i][1]:
            cur += result[i][2]
            
        else: # 다르면 열이 바뀐거니까 갱신 
            answer = max(cur, answer)
            cur = result[i][2]
    
    answer = max(cur,answer)
    return answer