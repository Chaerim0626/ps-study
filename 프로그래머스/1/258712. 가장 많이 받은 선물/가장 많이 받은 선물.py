
def solution(friends, gifts):
    
    # 두 사람이 선물을 주고받은 기록이 있다면, 더 많이 주면 다음 달 하나 
    # 기록없거나 같으면 선물지수 크면 -> 작은 사람에게 
    
    # 선물지수: 친구들에게 준 선물의 수 - 받은 선물의 수 
    # 다음 달에 가장 많은 선물을 받는 친구의 받을 선물의 수 return 
    
    n = len(friends)
    table = [[0] * n for _ in range(n)]
    result = [0] * n
    gift_index = [0] * n
    
    for gift in gifts:
        give, take = gift.split(" ")
        give_idx, take_idx = friends.index(give), friends.index(take)
        gift_index[give_idx] += 1
        gift_index[take_idx] -= 1
        table[give_idx][take_idx] += 1
    
    
    for i in range(n):
        for j in range(i+1,n):
            if table[i][j] > table[j][i]:
                result[i] += 1
            elif table[i][j] < table[j][i]:
                result[j] += 1
            else:
                if gift_index[i] > gift_index[j]:
                    result[i] += 1
                elif gift_index[i] < gift_index[j]:
                    result[j] += 1
                    
    
    return max(result)
