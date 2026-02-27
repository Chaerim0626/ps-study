import sys 
input = sys.stdin.readline 


a,b = input().strip().split(' ')

len_a = len(a)
len_b = len(b)
diff = len_b - len_a

def sol(a,b,result):
    for i in range(len_b):
        if a[i] != b[i]:
            result += 1
    return result 
    
if len_a == len_b:
    res = sol(a,b,0)
    print(res)
else:
    best = float('inf')
    for i in range(diff + 1):          # 여기: 오프셋 루프
        n = 0
        for j in range(len_a):
            if a[j] != b[j + i]:       # 여기: i(오프셋) 반영!
                n += 1
        best = min(best, n)      # 여기: 패딩 차이도 고려
    print(best)