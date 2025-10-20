import sys 
input = sys.stdin.readline 
from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input().rstrip())
    clothes = defaultdict(list)
    for _ in range(n):
        a,b = input().split(' ')
        b = b.strip()
        
        clothes[b].append(a)
    
    result = 1
    
    for v in clothes.values():
        result *= (len(v) + 1)  # 입거나 안 입거나
        
    print(result-1)
    
    