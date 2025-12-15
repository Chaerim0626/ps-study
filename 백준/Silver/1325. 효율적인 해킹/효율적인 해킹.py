import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n, m = map(int, input().split())

# 역방향 그래프
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

def dfs(start):
    stack = [start]
    visited = [0] * (n + 1)
    visited[start] = 1
    cnt = 1

    while stack:
        cur = stack.pop()
        for nxt in graph[cur]:
            if not visited[nxt]:
                visited[nxt] = 1
                cnt += 1
                stack.append(nxt)
    return cnt

max_cnt = 0
result = []

for i in range(1, n + 1):
    c = dfs(i)
    if c > max_cnt:
        max_cnt = c
        result = [i]
    elif c == max_cnt:
        result.append(i)

print(*result)
