import sys 
input = sys.stdin.readline 

# N - 10만 
n = int(input())
arr = []
for _ in range(n):
    start, end = map(int,input().split())
    arr.append((start,end))

arr.sort(key=lambda x: (x[1],x[0]))


result = 1

start,end = arr[0][0], arr[0][1] #기준 점이 되는게 끝나는게 가장 빠른 방 (1,4)

for i in range(1,n):
    if end <= arr[i][0]:
        end = arr[i][1]
        result += 1
    else:
        pass
    
print(result)