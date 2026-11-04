from collections import deque

# S 시작, E 출구, L 레버, O통로, X벽
def isvalid(x,y,maps):
    return 0 <= x < len(maps) and 0 <= y < len(maps[0])

def bfs(sx,sy,maps):
    dq = deque([(sx,sy,0)])
    visited = set()
    visited.add((sx,sy))
    dir = [(0,1), (0,-1), (1,0), (-1,0)]
    
    while dq:
        cx,cy,cnt = dq.popleft()
        if maps[cx][cy] == 'L':
            return cnt 
        
        for dx,dy in dir:
            nx,ny = cx+dx, cy+dy
            if (nx,ny) not in visited:
                if isvalid(nx,ny,maps) and maps[nx][ny] != 'X':
                    dq.append((nx,ny,cnt+1))
                    visited.add((nx,ny))
                
    return -1

def bfs2(sx,sy,maps):
    dq = deque([(sx,sy,0)])
    visited = set()
    visited.add((sx,sy))
    dir = [(0,1), (0,-1), (1,0), (-1,0)]
    
    while dq:
        cx,cy,cnt = dq.popleft()
        if maps[cx][cy] == 'E':
            return cnt 
        
        for dx,dy in dir:
            nx,ny = cx+dx, cy+dy
            if (nx,ny) not in visited:
                if isvalid(nx,ny,maps) and maps[nx][ny] != 'X':
                    dq.append((nx,ny,cnt+1))
                    visited.add((nx,ny))
                
    return -1
    
def solution(maps):
    
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                cnt = bfs(i,j,maps)
                
            elif maps[i][j] == 'L':
                cnt2 = bfs2(i,j,maps)
    return cnt+cnt2 if cnt != -1 and cnt2 != -1 else -1 