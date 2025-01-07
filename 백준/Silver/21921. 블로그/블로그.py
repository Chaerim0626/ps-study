import sys
input = sys.stdin.readline 

n,x = map(int,input().split())
visited = list(map(int,input().split()))

current = 0
result = 0
cnt = 0

left, right = 0,0

while right < n:
    current += visited[right]

    if right - left + 1 > x:
        current -= visited[left]
        left += 1

    if right - left +1   == x:
        if current > result:
            result = current 
            cnt = 1
        elif current == result:
            cnt += 1
    right += 1

if not result:
    print("SAD")
else:
    print(result)
    print(cnt)
