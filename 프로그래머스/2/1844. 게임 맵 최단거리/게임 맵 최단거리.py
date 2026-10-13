from collections import deque

def solution(maps):
    # 0은 벽이 있는 자리, 1은 벽이 없는 자리 
    n,m = len(maps), len(maps[0])
    
    def isvalid(x,y):
        return 0 <= x < n and 0 <= y < m 
    def bfs(sx,sy,graph):
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        dq = deque([(sx,sy,1)])
        visited = [[0]*m for _ in range(n)]
        visited[sx][sy] = 1 
        
        while dq:
            cx,cy,cnt = dq.popleft()
            
            if cx == (n-1) and cy == (m-1):
                return cnt  
            
            for dx,dy in dir:
                nx,ny = cx+dx, cy+dy 
                
                if isvalid(nx,ny):
                    if not visited[nx][ny]:
                        if graph[nx][ny] == 1:
                            dq.append((nx,ny,cnt+1))
                            visited[nx][ny] = 1
        return -1 
    answer = bfs(0,0,maps)
    return answer