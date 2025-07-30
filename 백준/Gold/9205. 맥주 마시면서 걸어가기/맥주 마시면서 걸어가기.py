import sys
from collections import deque 

input = sys.stdin.readline 

t = int(input())


def bfs(sx,sy,fx,fy,loc):

    visited = dict()
    visited[sx,sy] = 1
    dq = deque([(sx,sy)])

    
    while dq:
        cx,cy = dq.popleft()

        if cx == fx and cy == fy:
            return "happy"
                        
        for nx, ny in loc:
            if abs(cx-nx) + abs(cy-ny) <= 1000:
                if (nx,ny) not in visited:
                    dq.append((nx,ny))
                    visited[nx,ny] = 1
    return "sad"

for _ in range(t):
    n = int(input())
    loc = []
    
    hx,hy = map(int,input().split())
    
    for _ in range(n):
        cx,cy = map(int,input().split())
        loc.append((cx,cy))
        
    fx,fy = map(int,input().split())
    loc.append((fx,fy))


    s = bfs(hx,hy,fx,fy,loc)
    print(s)

