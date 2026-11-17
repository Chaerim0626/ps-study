def solution(bandage, health, attacks):
    answer = 0
    # 1초마다 x만큼의 체력 회복 t*x + y 
    # 기술이 취소 당하거나, 기술이 끝나면 즉시 붕대감기
    # 연속 성공시간 0으로 초기화 
    max_health, hp = health, health
    # bandage: t, x, y
    t,x,y = bandage 
    # t2, at = attacks
    streak = 0
    max_health = health 
    dic = dict()
    
    for i, j in attacks:
        dic[i] = j 

    for i in range(attacks[-1][0]+1):
        
        if i not in dic: # 공격 초가 아닐때
            hp += x
            streak += 1
            if streak == t: 
                hp += y 
                streak = 0
        else: 
            streak = 0
            hp -= dic[i]
        
        if hp > max_health:
            hp = max_health
        elif hp <= 0:
            return -1
    
    return hp