def solution(keymap, targets):
    answer = []
    dic = dict()
    
    for i in range(len(keymap)):
        for j in range(len(keymap[i])):
            if keymap[i][j] not in dic:
                dic[keymap[i][j]] = j+1
            else:
                dic[keymap[i][j]] = min(j+1,dic[keymap[i][j]])
                
    for i in range(len(targets)):
        cnt = 0
        flag = True 
        for j in range(len(targets[i])):
            if targets[i][j] not in dic:
                answer.append(-1)
                flag = False
                break 
            else:
                cnt += dic[targets[i][j]]
        if not flag:
            pass
        else:
            answer.append(cnt)
    
    return answer