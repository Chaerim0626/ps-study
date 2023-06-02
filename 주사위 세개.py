#단계별로 풀어보기 2. 조건문
# 2480 브론즈4

import sys
input = sys.stdin.readline
a,b,c = map(int,input().split())

if a == b and b == c:
    print(10000+a*1000)
elif a != b and b != c and a != c :
    print(max(a,(max(b,c)))*100)
else: #파이썬 여러조건 한줄에 쓰기
    #res = A if 조건1 else B if 조건2 else C
    print(1000+a*100) if a==b else print(1000+b*100) if b == c else print(1000+c*100)