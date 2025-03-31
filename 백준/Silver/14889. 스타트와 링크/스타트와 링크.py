import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**6)

n = int(input())
graph = []
for _ in range(n):
    s = list(map(int,input().split()))
    graph.append(s)
    
visited = [0] * n
result = float('inf')

def cal_diff(start, link):
    res, res2 = 0,0

    for i in range(len(start)):
        for j in range(i+1, len(start)):
            res += graph[start[i]][start[j]] + graph[start[j]][start[i]]
            res2 += graph[link[i]][link[j]] + graph[link[j]][link[i]]

    return abs(res-res2)
    
def backtracking(depth, idx):
    global result
    if depth == n//2:
        s,l = [],[]
        for i in range(n):
            if visited[i]:
                s.append(i)
            else:
                l.append(i)
        result = min(result,cal_diff(s,l))

        return 

    for i in range(idx, n):
        if visited[i] != 1:
            visited[i] = 1
            backtracking(depth+1, i)
            visited[i] = 0

backtracking(0,0)
print(result)
