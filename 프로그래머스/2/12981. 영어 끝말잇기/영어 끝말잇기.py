def solution(n, words):
    answer = []
    dic = dict()
    dic[words[0]] = 1
    for i in range(1,len(words)):
        
        if words[i-1][-1] != words[i][0]:
            answer.append(i%n+1)
            answer.append((i//n)+1)

            break 
        if words[i] not in dic:
            dic[words[i]] = 1
        elif words[i] in dic:
            answer.append(i%n+1)
            answer.append((i//n)+1)
            break 

    return answer if answer else [0,0]