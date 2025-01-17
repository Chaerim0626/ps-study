import sys
input = sys.stdin.readline 


n = int(input())
people = []
dic = dict()
rank = [0] * n

for idx in range(n):
    kg,cm = map(int,input().split())
    people.append(([kg,cm, idx]))
    
people.sort(key=lambda x:(-x[0],-x[1]))

cnt = 1

rank[people[0][2]] = 1

for i in range(n):
    kg,cm = people[i][0], people[i][1]
    for j in range(n):
        if i != j:
            if kg < people[j][0] and cm < people[j][1]:
                cnt += 1
    rank[people[i][2]] = cnt 
    cnt = 1
    
print(*rank)