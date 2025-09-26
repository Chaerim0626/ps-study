import sys 
from itertools import combinations
from collections import deque
input = sys.stdin.readline 

n,m = map(int,input().split())
graph = []

def chi_dist(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

for _ in range(n):
    graph.append(list(map(int,input().split())))

homes, chickens = [], []

# 집과 치킨의 좌표 저장
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            homes.append((i,j))
        elif graph[i][j] == 2:
            chickens.append((i,j))

# 치킨을 M만 고르는 조합 만들기
chics = list(combinations(chickens,m))
                    
min_result = float('inf')
for ch in chics:
    tmp = 0
    for hx,hy in homes:
        tmp += min(chi_dist(hx,hy,sx,sy) for sx, sy in ch)
    min_result = min(tmp,min_result)
print(min_result)
    


