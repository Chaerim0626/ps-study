import sys 
input = sys.stdin.readline 

s = input().rstrip()
bomb = input().rstrip()

st = []

for i in s:
    st.append(i)
    if st[len(st)-len(bomb):len(st)] == list(bomb):
        for _ in range(len(bomb)):
            st.pop()
if st:
    print(*st, sep='')
else:
    print('FRULA')