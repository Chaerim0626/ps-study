import sys 
input = sys.stdin.readline 
sys.setrecursionlimit(10**5)

n = int(input())
graph = []
graph2 = [[] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(n):
        if graph[i][j]:
            graph2[i].append(j)
    
# print(graph2)

result = [[0] * n for _ in range(n)]

def dfs(start,start2):
    global result, visited

    for next in graph2[start2]:
        # print(start, graph2[start2])
        if not visited[start2][next]:
            result[start][next] = 1
            visited[start2][next] = 1
            dfs(start,next)

for i in range(n):
    visited = [[0] * n for _ in range(n)]
    dfs(i,i)

for i in result:
    print(*i)
        
            
