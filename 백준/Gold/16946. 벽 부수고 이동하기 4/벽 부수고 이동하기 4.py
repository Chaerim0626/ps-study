import sys 
input = sys.stdin.readline 
from collections import deque

n, m = map(int, input().split())
graph = []

zeros = [[0] * m for _ in range(n)]
visited = [[0] * m for _ in range(n)]
result = [[0] * m for _ in range(n)]
dir = [(0,1), (0,-1),(1,0),(-1,0)]
group = 1
dic = dict()

for _ in range(n):
    row = list(map(int, input().strip()))  # 문자열을 문자 하나씩 분리
    graph.append(row)

def isvalid(x,y):
    return 0 <= x < n and 0 <= y < m
    
def bfs(sx,sy):
    dq = deque([(sx,sy)])
    visited[sx][sy] = 1
    cnt = 1
    while dq:
        cx,cy = dq.popleft()
        zeros[cx][cy] = group
        for dx,dy in dir:
            nx,ny = dx+cx,dy+cy 

            if isvalid(nx,ny) and not visited[nx][ny]:
                if not graph[nx][ny]:
                    cnt += 1
                    visited[nx][ny] = 1
                    dq.append((nx,ny))
    return cnt 

def move_cnt(x,y):
    s = set()

    for dx,dy in dir:
        nx,ny = dx+x,dy+y
        if isvalid(nx,ny) and zeros[nx][ny]:
            s.add(zeros[nx][ny])
    cnt = 1
    for c in s:
        cnt += dic[c] # 그룹 0 개수 추가 
        cnt %= 10 

    return cnt

    for c in s:
        cnt += info[c]
    
for i in range(n):
    for j in range(m):
        if not visited[i][j] and not graph[i][j]:
            cnt = bfs(i,j)
            dic[group] = cnt 
            group += 1

for i in range(n):
    for j in range(m):
        if graph[i][j]:
            result[i][j] = move_cnt(i,j)
#print(result)
for i in range(n):
    print("".join(map(str,result[i])))
    
        
    