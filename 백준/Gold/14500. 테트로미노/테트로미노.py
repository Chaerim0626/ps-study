import sys 
input = sys.stdin.readline 

n,m = map(int,input().split())
graph = []

for _ in range(n):
    row = list(map(int,input().split()))
    graph.append(row)

visited = [[0] * m for _ in range(n)]
max_result = 0

# 모든 좌표를 순회하며 모두 대어보고 최대값을 구해야함 
# 500*500*4*4 = 대충 400만

t1 = [[(0,0), (0,1), (0,2), (0,3)], [(0,0), (1,0), (2,0), (3,0)]]
t2 = [[(0,0), (0,1), (1,0), (1,1)]]

t3 =[[(0,0), (1,0), (2,0), (2,1)], [(0,0), (0,1), (0,2), (1,0)], 
     [(0,0), (0,1), (1,1), (2,1)],[(0,2), (1,0), (1,1), (1,2)], 
     [(0,0), (0,1), (1,0), (2,0)], [(0,0), (0,1), (0,2), (1,2)],
     [(0,1), (1,1), (2,1), (2,0)], [(0,0), (1,0), (1,1), (1,2)]]

t4 = [[(0,0), (0,1), (0,2), (1,1)], [(0,1), (1,0), (1,1), (1,2)], 
      [(0,0), (1,0), (1,1), (2,0)],[(0,1), (1,0), (1,1), (2,1)]]

t5 = [[(0,0), (1,0), (1,1), (2,1)], [(0,1), (0,2), (1,0), (1,1)], 
      [(0,1), (1,0), (1,1), (2,0)],[(0,0), (0,1), (1,1), (1,2)]]

def isvalid(x,y,t_arr):
    tmp2 = 0
    for i in range(len(t_arr)):
        tmp = 0
        for a,b in t_arr[i]:
            if x+a >= n or y+b >= m:
                break
            else:
                tmp += graph[x+a][y+b]
        tmp2 = max(tmp,tmp2)
    return tmp2

result = 0
for i in range(n):
    
    for j in range(m):
        
        if isvalid(i,j,t1):
            result = max(result,isvalid(i,j,t1))

        if isvalid(i,j,t2):
            result = max(result,isvalid(i,j,t2))

        if isvalid(i,j,t3):
            result = max(result,isvalid(i,j,t3))

        if isvalid(i,j,t4):
            result = max(result,isvalid(i,j,t4))

        if isvalid(i,j,t5):
            result = max(result,isvalid(i,j,t5))

print(result)
        

    
