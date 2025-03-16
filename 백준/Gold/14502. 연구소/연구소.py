import sys
from collections import deque
input = sys.stdin.readline

# 백트래킹을 활용한 벽 설치
def backtrack(cnt, idx):
    if cnt == 3:  # 벽을 3개 설치하면 BFS 실행
        tmp_graph = [row[:] for row in graph]  # 원본 그래프 복사
        bfs(tmp_graph)
        return
    
    for i in range(idx, len(walls)):
        x, y = walls[i]
        graph[x][y] = 1  # 벽 설치
        backtrack(cnt + 1, i + 1)
        graph[x][y] = 0  # 백트래킹 (원상 복구)

# BFS를 이용한 바이러스 확산
def bfs(tmp_graph):
    global result
    dq = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                dq.append((i, j))  # 초기 바이러스 위치 추가

    while dq:
        y, x = dq.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= ny < n and 0 <= nx < m and tmp_graph[ny][nx] == 0:
                tmp_graph[ny][nx] = 2
                dq.append((ny, nx))

    result = max(result, count_safe_area(tmp_graph))  # 최대 안전 영역 갱신

# 안전 영역(0 개수) 계산
def count_safe_area(tmp_graph):
    return sum(row.count(0) for row in tmp_graph)

# 입력 처리
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
walls = []  # 벽을 세울 수 있는 후보 좌표
result = 0  # 최대 안전 영역 크기

# 벽을 세울 수 있는 위치 저장
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            walls.append((i, j))

# 상하좌우 이동 방향 정의
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# 백트래킹 시작
backtrack(0, 0)

# 결과 출력
print(result)
