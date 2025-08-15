import sys
input = sys.stdin.readline 

n = int(input())
nums = list(map(int,input().split()))
oper = list(map(int,input().split()))

st = [nums[0]]
res = []

def cal(n,a,b):
    if n == 0:
        return a+b
    elif n == 1:
        return a-b
    elif n == 2:
        return a*b
    else:
        if a < 0 and b > 0:
            return -((-a)//b)
        elif a < 0 and b < 0:
            return -a // -b
        else:
            return a//b

def backtracking(idx):

    if idx == n:
        res.append(st[-1])
        return 
        
    for i in range(4):
            
        if oper[i] > 0:
            a = st[-1]
            b = nums[idx]

            st.append(cal(i,a,b))
            oper[i] -= 1
            backtracking(idx+1)
            st.pop()
            oper[i] += 1
        

backtracking(1)
print(max(res))
print(min(res))