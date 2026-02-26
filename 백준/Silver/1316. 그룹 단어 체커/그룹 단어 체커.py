import sys 
input = sys.stdin.readline 

n = int(input())
result = n
for _ in range(n):
    word = input().rstrip()
    dict = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
    start = 0
    dict[word[start]] += 1
    for i in range(1,len(word)):
        #print(start,i)
        if word[start] == word[i] and dict[word[i]] >= 1:
            start = i
        elif start != word[i]:
            dict[word[i]] += 1 
            start = i
        else:
            dict[word[i]] += 1
    for key, value in dict.items():
        if value >= 2:
            result -= 1
            break
print(result)
    
    