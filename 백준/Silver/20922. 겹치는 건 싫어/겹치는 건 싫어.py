import sys
input = sys.stdin.readline 
from collections import defaultdict

n,k = map(int,input().split())
nums = list(map(int,input().split()))
dic = defaultdict(int)

left,right = 0,0
cur_cnt = 0
result = 0

while right < n:

    dic[nums[right]] += 1

    while dic[nums[right]] > k:
        dic[nums[left]] -= 1
        left += 1
        result = max(result,cur_cnt)
        cur_cnt -= 1

    if dic[nums[right]] <= k:
        cur_cnt += 1

    
    right += 1

result = max(result,cur_cnt)
print(result)