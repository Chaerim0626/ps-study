import sys 
input = sys.stdin.readline 

n,k = map(int,input().split())
temperatures = list(map(int,input().split()))


s = sum(temperatures[:k])       # 첫 창문 합
res = s

for i in range(1, n - k + 1):
    s -= temperatures[i - 1]     # 왼쪽에서 빠지는 놈
    s += temperatures[i + k - 1] # 오른쪽에서 들어오는 놈
    res = max(res, s)

    
print(res)