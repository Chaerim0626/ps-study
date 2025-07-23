def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    
    # 예외 처리 현재위치 10초미만, 남은시간 10초미만
    # video_len 보다 pos가 작은지 항상 확인 
    
    
    v_minutes, v_seconds = int(video_len[:2]), int(video_len[3:])
    p_minutes, p_seconds = int(pos[:2]), int(pos[3:])
    
    op_s_minutes, op_s_seconds = int(op_start[:2]), int(op_start[3:])
    op_e_minutes, op_e_seconds = int(op_end[:2]), int(op_end[3:])
    
    
    v, p = v_minutes*60 + v_seconds, p_minutes*60 + p_seconds 
    op_s, op_e = op_s_minutes*60 + op_s_seconds, op_e_minutes*60 + op_e_seconds
    
    for cmd in commands:

        if op_s <= p and p <= op_e:
            p = op_e
            
        if cmd == 'next':
            p += 10
            if p > v:
                p = v 
        
        else:
            p -= 10 
            if p < 0:
                p = 0
      
    
    if op_s <= p and p <= op_e:
        p = op_e
    
    tmp, tmp2 = str(p//60), str(p%60)

    if p//60 < 10:
        tmp = '0'+str(p//60)
    if p%60 < 10:
        tmp2 = '0'+str(p%60)
    
    answer = tmp+':'+tmp2

    return answer