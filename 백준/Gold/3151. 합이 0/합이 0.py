import sys
input = sys.stdin.readline 

n = int(input())
nums = list(map(int,input().split()))
nums.sort()
result = 0


for i in range(n-2):
    start = nums[i]
    left,right = i+1,n-1


    if start > 0:
        break
        
    while left < right:
        tot = nums[left] + nums[right]

        if start + tot == 0:
            
            if nums[left] == nums[right]:
                count = right - left + 1
                result += count * (count - 1) // 2
                break
            
            left_tmp,right_tmp = 1,1
            
            while left+1 < right and nums[left] == nums[left+1]  :
                left_tmp += 1
                left += 1

            while left < right-1 and nums[right] == nums[right-1]:
                right_tmp += 1
                right -=1 

            result += left_tmp*right_tmp
            left += 1
            right -= 1
            
        elif start + tot < 0: # 음수면 left += 1
            left += 1
        else:
            right -= 1



print(result)