from collections import deque, defaultdict

def topological_sort_bfs(n, edges):

    graph = defaultdict(list)
    indegree = [0] * n

    for u, v in edges:
        graph[u].append(v)
        indegree[v] += 1

    dq = deque([i for i in range(n) if indegree[i] == 0])
    result = []

    while dq:
        node = dq.popleft()
        result.append(node)
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                dq.append(nxt)

    if len(result) != n:
        return []  # 사이클 존재
    return result


n,m  = map(int,input().split())
edges = []

for _ in range(m):
    a,b = map(int,input().split())
    edges.append((a-1,b-1))

result = topological_sort_bfs(n,edges)

print(*[x+1 for x in result])