def solution(bandage, health, attacks):
    # bandage - [시전 시간, 회복량, 추가회복량], attacks - [공격시간, 피해량]
    
    time = [0] * (attacks[-1][0] + 1)
    time[0] = health
    at = [i for i,j in attacks]

    cont = 0
    cnt = 0
    flag = True 

    for i in range(1,len(time)):
        
        if i not in at:
            time[i] = time[i-1]
            cont += 1
            if cont == bandage[0]:
                time[i] = time[i-1] + bandage[1] + bandage[2]
                cont = 0
            
            else:
                time[i] = time[i-1] + bandage[1]
            
        else:
            cont = 0 
            time[i] = time[i-1] - attacks[cnt][1] 
            cnt += 1
            if time[i] <= 0 :
                flag = False 
                break 
                
        if not flag:
            break
        
        if time[i] > health:
            time[i] = health

    answer = time[-1] if flag else -1
    return answer