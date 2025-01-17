import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**6)

n,m = map(int,input().split())
graph  = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
result = 0
visited = [0] * n


def dfs(start,cnt):
    global result

    if cnt == 5:
        result = 1
        return
        
    visited[start] = 1
    
    for node in graph[start]:
        if not visited[node]:
            dfs(node,cnt+1)

    visited[start] = 0
    return

for i in range(n):
    dfs(i,1)
    if result:
        break


print(result)