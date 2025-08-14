import sys 
from collections import deque
input = sys.stdin.readline

# 낮은 칸과 높은 칸의 높이 차이는 1 
# 개수는 엄청 많은데 L개의 칸 연속 

n,l = map(int,input().split())
graph = []
for _ in range(n):
    height = list(map(int,input().split()))
    graph.append(height)


result = 0

def rotate(arr):
    rotated = list(map(list, zip(*arr[::-1])))
    return rotated 

# 계단을 자꾸 겹쳐서 쌓는 부분을 구현으로 해결하지 못하고 있음 ㅜ 

def check_road(graph): # 1차원 배열을 인자로 받기
    visited = [0] * n  # 경사로 만들었는지 체크하는 배열
    
    for i in range(n-1):
        if abs(graph[i] - graph[i+1]) > 1:
            return False
                
        elif graph[i] == graph[i+1]:
            continue 
                
        elif graph[i] < graph[i+1]:
            tmp = graph[i]
            
            # 증가하는 경우 발견하면 l만큼 뒤로갈수있는지 체크, 계단을 무조건 만들긴 해야함
            for j in range(i, i-l, -1):
                if j < 0:
                    return False 
                    
                if visited[j] or tmp != graph[j]:
                    return False 

                visited[j] = 1
    
        else:  # 1칸 감소하는 경우 l만큼 앞으로 갈 수 있는지 체크
            tmp = graph[i+1]
            
            for j in range(i+1,i+1+l):
                if j > (n-1):
                    return False 
                if visited[j] or tmp != graph[j]:
                    return False
                visited[j] = 1
                
    return True
                

for i in range(n):
    if check_road(graph[i]):
        #print(graph[i])
        #print(check_road(graph[i]))
        result += 1

#print(result)
#print('--------회전-----------')
graph = rotate(graph)

for i in range(n):
    if check_road(graph[i]):
        #print(graph[i])
        #print(check_road(graph[i]))
        result += 1
print(result)
        