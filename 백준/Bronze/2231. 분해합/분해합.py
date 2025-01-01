import sys
input = sys.stdin.readline 

n = int(input())
tot = 0

for i in range(1,n):

    for j in range(len(str(i))):
        tot += int(str(i)[j])
    tot += i

    if tot == n:
        print(i)
        break 

    tot = 0
if not tot:
    print(0)