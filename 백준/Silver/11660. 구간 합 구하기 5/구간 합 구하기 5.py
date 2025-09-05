import sys 
input = sys.stdin.readline 

n,m = map(int,input().split())
graph = []
for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

dp = [[0] * n for _ in range(n)]

dp[0][0] = graph[0][0]

for i in range(1,n):
    dp[i][0] = dp[i-1][0] + graph[i][0]
    dp[0][i] = dp[0][i-1] + graph[0][i]

for i in range(1,n):
    for j in range(1,n):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] + graph[i][j] - dp[i-1][j-1]


for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    x1,y1 = x1-1,y1-1
    x2,y2 = x2-1,y2-1


    if x1 == x2 and y1 == y2:
        print(graph[x2][y2])
    elif x1 == 0 and y1 == 0:
        print(dp[x2][y2])
    elif x1 == 0 and y1 != 0:
        print(dp[x2][y2] - dp[x2][y1-1])
    elif x1 != 0 and y1 ==0:
        print(dp[x2][y2] - dp[x1-1][y2])
    else:
        print(dp[x2][y2]-dp[x1-1][y2]-dp[x2][y1-1]+dp[x1-1][y1-1])

        
        


    
    