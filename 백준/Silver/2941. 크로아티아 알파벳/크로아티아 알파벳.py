import sys 
input = sys.stdin.readline 
s = input().rstrip()
for p in ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
    s = s.replace(p, '#')
print(len(s))