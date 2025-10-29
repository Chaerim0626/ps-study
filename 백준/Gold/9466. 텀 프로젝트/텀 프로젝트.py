import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**6) 

def dfs(i):
    global count 

    visited[i] = 1
    cycle_list.append(i)

    if visited[nums[i]]:
        if nums[i] in cycle_list:
            count -= len(cycle_list[cycle_list.index(nums[i]):])
        return 
    else:
        dfs(nums[i])
t = int(input())
for _ in range(t):
    n = int(input())

    nums = [0]
    nums.extend([int(x) for x in input().split()])

    visited = [0] * (n+1)
    count = n

    for i in range(1,n+1):
        if not visited[i]:
            cycle_list = []
            dfs(i)
            #print(cycle_list)
    print(count)
        