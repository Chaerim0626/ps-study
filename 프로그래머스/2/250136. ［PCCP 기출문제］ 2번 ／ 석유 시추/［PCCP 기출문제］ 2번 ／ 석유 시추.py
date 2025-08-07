import copy
from collections import deque

def solution(land):
    
    n, m = len(land), len(land[0]) # 500*500이 최대 크기
    visited = [[0] * m for _ in range(n)]

    def isvalid(x,y):
        return 0 <= x < n and 0 <= y < m
    
    # 일단 bfs()로 1이 엮여있는 영역 크기를 세자. 
    # 영역도 번호를 붙여서 directory로 번호: 영역크기로 저장할까? 그래서 set으로 중복없애서 영역 셀 수 있게 
    # 그럼 일단 solution에 for for 돌려서 1이 나오면 그때 visit체크, 영역 세기를 해야하나
    # 원본 land는 남겨놓고 copy써야할듯 

    result = [0]  * m
    
    # 이건 최단경로가 아니라 영역 크기를 세는거
    def bfs(sx,sy):
        
        dq = deque([(sx,sy)])
        cnt = 1
        visited[sx][sy] = 1
        dir = [(0,1), (0,-1), (1,0), (-1,0)]
        tmp = set()
        tmp.add(sy)
        
        # 같은 영역에서는 ny가 다르면됨
        while dq:
            cx,cy = dq.popleft()
            
            for dx,dy in dir:
                nx,ny = cx+dx, cy+dy
                
                if isvalid(nx,ny) and not visited[nx][ny]:
                    if land[nx][ny]:
                        cnt += 1
                        tmp.add(ny)
                        dq.append((nx,ny))
                        visited[nx][ny] = 1
    
        return cnt,tmp
    
    tmp_set = set()
    for i in range(n):
        for j in range(m):
            if land[i][j] and not visited[i][j]:
                cnt, tmp_set = bfs(i,j)
                for k in tmp_set:
                    result[k] += cnt
                    
    return max(result)