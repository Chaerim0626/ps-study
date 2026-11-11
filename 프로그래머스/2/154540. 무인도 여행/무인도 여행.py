from collections import deque 

def solution(maps):
    answer = []
    m,n = len(maps[0]),len(maps)
    flag = False
    for row in maps:
        for i in row:
            if i in '123456789':
                flag = True 
    if not flag:
        return [-1]
    
    visited = [[0] * m for _ in range(n)]
    # X는 바다, 숫자는 무인도
    def bfs(sx,sy):
        nonlocal cnt 
        dq = deque([(sx,sy)])
        visited[sx][sy] = 1
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while dq:
            cx,cy = dq.popleft()
            for dx,dy in dir:
                nx,ny = cx+dx, cy+dy
                
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and maps[nx][ny] in '123456789':
                        visited[nx][ny] = 1
                        dq.append((nx,ny))
                        cnt += int(maps[nx][ny])
        return cnt 
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and maps[i][j] in '123456789':
                cnt = int(maps[i][j])
                answer.append(bfs(i,j))
    
    return sorted(answer)