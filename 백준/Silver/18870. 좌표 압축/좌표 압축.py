import sys
input = sys.stdin.readline 

n = int(input())
nums = list(map(int,input().split()))
coordinate = []

for i in range(n):
    coordinate.append([i,nums[i]]) # 1- 좌표와 인덱스 추가
#print(coordinate)
coordinate.sort(key=lambda x:x[1]) # 2- 뒤 숫자(좌표) 기준 정렬
#print(coordinate)

# 3- 좌표값을 0부터 반복문으로 변경
result = [[coordinate[0][0], 0]]
for i in range(1,n):
    if coordinate[i-1][1] == coordinate[i][1]:
        result.append([coordinate[i][0],result[-1][1]])
    else:
        result.append([coordinate[i][0],result[-1][1]+1])
#print(result)

# 4 - 인덱스 기준 다시 정렬
result.sort(key=lambda x:x[0])

#print(result)
for _,i in result:
    print(i, end=' ')
    