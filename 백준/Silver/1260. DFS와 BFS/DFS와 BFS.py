import sys
input = sys.stdin.readline 
from collections import deque


n,m,start = map(int,input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

for i in graph:
    i.sort()

visited = [0] * (n+1)

def dfs(node):

    print(node, end=' ')
    visited[node] = 1

    for next in graph[node]:
        if not visited[next]:
            dfs(next)


dfs(start)

visited = [0] * (n+1)
def bfs(node):

    dq = deque()
    dq.append(node)
    visited[node] = 1

    while dq:
        node = dq.popleft()
        print(node, end =' ')
        for next in graph[node]:
            if not visited[next]:
                visited[next] = 1
                dq.append(next)
print()
bfs(start)