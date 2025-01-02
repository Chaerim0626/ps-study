import sys
input = sys.stdin.readline 

n,k = map(int,input().split())
nums = list(map(int,input().split()))
cnt = 0
result = 0
cur_sum = 0

left,right = 0,0

while right < n:
    
    if nums[right] % 2 == 0:
        cur_sum += 1
    else:
        cnt += 1

    
    while cnt > k:
        if nums[left] % 2 == 0:
            cur_sum -= 1
        else:
            cnt -= 1
        left += 1

    result = max(result,cur_sum)
    right += 1

result = max(result,cur_sum)
print(result)