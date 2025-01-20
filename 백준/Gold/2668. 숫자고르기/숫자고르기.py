import sys
input = sys.stdin.readline 

n = int(input())
numbers = [0] * (n+1)

for i in range(1,n+1):
    numbers[i] = (int(input()))
# n^3도 가능, DFS
# i+1과 자기자신이 같은 경우
result = []

def dfs(start):    

    visited[start] = 1
    tmp_idx.append(start)
    tmp_set.append(numbers[start]) # [idx,원소]
    
    if not visited[numbers[start]]:
        dfs(numbers[start])
        

for i in range(1,n+1):
    visited = [0] * (n+1)
    tmp_idx = []
    tmp_set = []
    dfs(i)

    if len(tmp_set) == 1 and tmp_set[0] == tmp_idx[0]:
        result.append(tmp_set[0])
        
    elif set(tmp_idx) == set(tmp_set):
        for i in tmp_set:
            result.append(i)
            
    
result = set(result)
print(len(result))
for i in sorted(result):
    print(i)