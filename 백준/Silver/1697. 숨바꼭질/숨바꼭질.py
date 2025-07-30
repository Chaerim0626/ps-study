import sys
from collections import deque 

n,k = map(int,input().split())

def bfs(n,k):
    visited = [0] * 200001
    visited[n] = 1
    dq = deque([(n,0)])

    while dq:
        cx,cnt = dq.popleft()

        if cx == k:
            return cnt
            
        for d in [2*cx,cx+1,cx-1]:

            if 0 <= d and d <= 100000:
                if not visited[d]:
                    visited[d] = 1
                    dq.append((d,cnt+1))

if n == k:
    print(0)
else:
    print(bfs(n,k))
                