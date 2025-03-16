import sys, copy
from collections import deque

input = sys.stdin.readline

def isvalid(x, y):
    return 0 <= x < n and 0 <= y < m

# BFS를 이용한 바이러스 확산
def bfs(arr):
    dq = deque(virus)  
    visited = [[0]*m for _ in range(n)]
    directions = [(0,1), (0,-1), (1,0), (-1,0)]

    while dq:
        cx, cy = dq.popleft()
        for dx, dy in directions:
            nx, ny = cx + dx, cy + dy

            if isvalid(nx, ny) and not visited[nx][ny]:
                if arr[nx][ny] == 0:
                    arr[nx][ny] = 2
                    visited[nx][ny] = 1
                    dq.append((nx, ny))

    return sum(row.count(0) for row in arr)

# 백트래킹을 이용한 벽 설치
def backtrack(cnt):
    global result
    if cnt == 3:  # 벽 3개 설치 완료
        tmp_graph = copy.deepcopy(graph)
        result = max(result, bfs(tmp_graph))
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:  # 빈칸이면 벽 설치
                graph[i][j] = 1
                backtrack(cnt + 1)
                graph[i][j] = 0  # 백트래킹 (원상 복구)

# 입력 처리
n, m = map(int, input().split())
graph = []
virus = []
result = 0

for _ in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append((i, j))

# 백트래킹 실행
backtrack(0)
print(result)
