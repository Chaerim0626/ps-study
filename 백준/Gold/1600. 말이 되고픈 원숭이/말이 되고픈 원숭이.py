import sys
import heapq

input = sys.stdin.readline 

k = int(input())
w, h = map(int, input().split())
graph = []

for _ in range(h):
    graph.append(list(map(int, input().split())))

# 기본 이동 방향 (상하좌우)
dir_normal = [[0, 1], [0, -1], [-1, 0], [1, 0]]
# 말 이동 방향 (8가지)
dir_horse = [[2, 1], [2, -1], [1, 2], [1, -2], 
             [-2, -1], [-1, -2], [-2, 1], [-1, 2]]

# 방문 배열 (2차원)
visited = [[-1] * w for _ in range(h)]

def isvalid(x, y):
    return 0 <= x < h and 0 <= y < w

def bfs():
    pq = []
    heapq.heappush(pq, (0, 0, 0, 0))  # (move, x, y, 말 이동 횟수)
    visited[0][0] = 0  # 시작 지점의 말 이동 횟수 기록

    while pq:
        move, sx, sy, scnt = heapq.heappop(pq)

        # 목표 지점 도착 확인
        if sx == h - 1 and sy == w - 1:
            return move

        # 일반 이동 (상하좌우)
        for dx, dy in dir_normal:
            nx, ny = sx + dx, sy + dy
            if isvalid(nx, ny) and not graph[nx][ny]:
                if visited[nx][ny] == -1 or visited[nx][ny] > scnt:
                    visited[nx][ny] = scnt
                    heapq.heappush(pq, (move + 1, nx, ny, scnt))

        # 말 이동 (8방향), 남은 횟수(scnt)가 k 미만일 때만 실행
        if scnt < k:
            for dx, dy in dir_horse:
                nx, ny = sx + dx, sy + dy
                if isvalid(nx, ny) and not graph[nx][ny]:
                    if visited[nx][ny] == -1 or visited[nx][ny] > scnt + 1:
                        visited[nx][ny] = scnt + 1
                        heapq.heappush(pq, (move + 1, nx, ny, scnt + 1))

    return -1

print(bfs())
