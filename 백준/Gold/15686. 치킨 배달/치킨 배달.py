import sys, copy
input = sys.stdin.readline 
from collections import deque
sys.setrecursionlimit(10**5)

n,m = map(int,input().split())
graph = []
for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

# m개의 치킨집 최대 

home = [(i,j) for i in range(n) for j in range(n) if graph[i][j] == 1]
loc = [(i,j) for i in range(n) for j in range(n) if graph[i][j] ==2]

visited_loc = [0] * len(loc)
res = []


res = float('inf')
g = copy.deepcopy(graph)
for x,y in loc:
    g[x][y] = 0

def backtracking(idx,cnt):

    global res 

    if cnt == m:
        total = 0
        for hx,hy in home:
            min_dist = float('inf')
            for k, (cx,cy) in enumerate(loc):
                if visited_loc[k]:
                    dist = abs(hx-cx) + abs(hy-cy)
                    min_dist = min(min_dist, dist)
            total += min_dist
        res = min(res,total)
        return 

    for i in range(idx,len(loc)):
        x,y = loc[i]
        g[x][y] = 2
        visited_loc[i] = 1
        backtracking(i+1,cnt+1) 
        g[x][y] = 0
        visited_loc[i] = 0


backtracking(0,0)
print(res)

