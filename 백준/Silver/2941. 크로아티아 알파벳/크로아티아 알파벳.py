import sys 
input = sys.stdin.readline 

cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
res = 0

cur = 0
s = input().rstrip()
while cur < len(s):

    if s[cur] in 'cdlnsz':
        if cur < len(s)-1:
            if s[cur] =='c' and (s[cur+1] == '=' or s[cur+1] == '-'):
                res += 1
                cur += 2 
                continue
            elif s[cur] == 'd':
                if cur < len(s)-2 and s[cur+1] == 'z' and s[cur+2] == '=':
                    res += 1
                    cur += 3
                    continue
                elif s[cur+1] == '-':
                    res += 1
                    cur += 2
                    continue
                else:
                    res += 1
            elif s[cur] == 'l' and s[cur+1] == 'j':
                res += 1
                cur += 2
                continue
            elif s[cur] == 'n' and s[cur+1] == 'j':
                res += 1
                cur += 2
                continue
            elif s[cur] =='s' and s[cur+1] == '=':
                res += 1
                cur += 2
                continue
            elif s[cur] =='z' and s[cur+1] == '=':
                res += 1
                cur += 2
                continue
            else:
                res += 1

        else:
            res += 1
    else:
        res += 1

    cur += 1
        
print(res)