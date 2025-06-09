import sys 
input = sys.stdin.readline 


t = int(input())
for _ in range(t):
    scores = []
    n = int(input())
    for _ in range(n):
        a,b = map(int,input().split())
        scores.append((a,b))
    result = 1
    scores.sort(key=lambda x: (x[0],x[1]))

    start,end = scores[0][0], scores[0][1]
    for i in range(1,n):
        if start < scores[i][0] and end < scores[i][1]:
            pass 
        else:
            result +=1 
            start,end = scores[i][0], scores[i][1]

    print(result)