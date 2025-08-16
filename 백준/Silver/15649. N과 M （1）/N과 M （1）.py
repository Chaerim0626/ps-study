import sys, copy
input = sys.stdin.readline 
n,m = map(int,input().split())

res = []
visited = [0] * (n+1)

# 중복 허용 x 순열

def backtracking(idx):
    if len(res) == m:
        print(' '.join(map(str,res)))
        return 

    for i in range(1,n+1):
        if not visited[i]:
            res.append(i)
            visited[i] = 1
            backtracking(i+1)
            res.pop()
            visited[i] = 0

backtracking(1)