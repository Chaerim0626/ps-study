import sys 
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
locations = list(map(int,input().split()))


pos = [loc for loc in locations if loc > 0]
neg = [-loc for loc in locations if loc < 0]

pos.sort(reverse=True)
neg.sort(reverse=True)

result = 0

for i in range(0,len(pos),m):
    result += pos[i]*2
for i in range(0,len(neg),m):
    result += neg[i]*2

max_dist = max(pos[0] if pos else 0, neg[0] if neg else 0)

print(result-max_dist)