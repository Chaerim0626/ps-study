import sys
input = sys.stdin.readline 

n = int(input())
li = list(map(int,input().split()))
li.sort()
tmp2 = float('inf')
result = [0,0]
left,right = 0, n-1

while left < right:
    tmp = li[left] + li[right]

    if abs(tmp) < abs(tmp2):
        tmp2 = tmp 
        result = [li[left],li[right]]


    if tmp > 0: # 0 보다 크니까 - 쪽으로
        right -= 1
    
    elif tmp < 0:
        left += 1
    else:
        result = [li[left], li[right]]
        break 

print(*result)