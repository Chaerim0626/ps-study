import sys

INF = float('inf')
input = sys.stdin.readline 

n,k = map(int,input().split())
coor = [] # 모든 좌표

for _ in range(n):
    a,b = map(int,input().split())
    coor.append((a,b))

chosen = []
result = INF

def dis(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def calc(selected):
    ans = 0
    for i in range(n): # 모든 집에 대해서
        min_dist = INF
        for s in selected: 
            d = dis(coor[i][0],coor[i][1],coor[s][0],coor[s][1])
            min_dist = min(min_dist,d) # 집 i와 가장 가까운 대피소 찾는 중 
        ans = max(ans,min_dist) # 가장 먼 집 기록

    return ans


def backtrack(start):
    global result 

    if len(chosen) == k:
        #print(chosen)
        result = min(result,calc(chosen))
        return 

    for i in range(start,n): # 중복 조합이 안생기게 하려면 start부터 시작해야함
        chosen.append(i)
        backtrack(i+1)
        chosen.pop()


backtrack(0)
print(result)
        