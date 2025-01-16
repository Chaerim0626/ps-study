import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())

def bfs(start):
    dq = deque()
    dq.append((start, 0))
    visited = [0] * 200001

    while dq:
        x, result = dq.popleft()

        if x == k:
            return result

        for d in range(3):
            if d == 0:
                nx = x * 2
                if 0 <= nx <= 200000 and not visited[nx]:
                    visited[nx] = 1
                    dq.appendleft((nx, result))  # 순간이동은 우선순위 높음
            elif d == 1:
                nx = x - 1
                if 0 <= nx <= 200000 and not visited[nx]:
                    visited[nx] = 1
                    dq.append((nx, result + 1))
            else:
                nx = x + 1
                if 0 <= nx <= 200000 and not visited[nx]:
                    visited[nx] = 1
                    dq.append((nx, result + 1))

print(bfs(n))
