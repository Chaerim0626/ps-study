import sys 
input = sys.stdin


def solve(s,t):
    idx = 0

    for i in t:
        if idx < len(s) and i == s[idx]:
            idx += 1
    return idx == len(s)

for line in sys.stdin:
    s,t = line.split()

    if solve(s,t):
        print('Yes')
    else:
        print("No")
    