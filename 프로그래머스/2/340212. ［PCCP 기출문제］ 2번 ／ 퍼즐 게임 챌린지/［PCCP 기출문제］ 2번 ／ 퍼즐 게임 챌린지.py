def solution(diffs, times, limit):
    # n개, 난이도 diff, 내 숙련도 level
    
    # diff <= level , 시간은 time_cur만큼 씀 
    # diff > level, diff - level번 틀림, 틀릴 때마다 += time_cur, 추가로 time_prev 만큼 써서 이전퍼즐도 다시 풀어야함 
    # 이전 퍼즐 풀때는 틀리지 않음 
    # 결국 틀릴때마다 (diff-level) * (time_prev + time_cur) 만큼 사용하고  + time_cur
    
    # level의 최소값을 구해야함 
    
    # times[i-1], time[i] 
    
    start, end = min(diffs), max(diffs)
    
    # 이분탐색이면 생각해봐야할 것 : mid랑 return 기준 

    time = times[0]
    
    while start <= end:
        time = times[0]
        mid = (start+end)//2
        
        #print(start,end,mid)
        for i in range(1,len(diffs)):
            if diffs[i] <= mid:
                time += times[i] 
            else:
                time += (diffs[i]-mid) * (times[i-1]+times[i]) + times[i]

        if limit < time:
            start = mid + 1
        else: # limit >= time
            answer = mid
            end = mid-1
        
        #print('time: ', time, mid)
            
        
    #print(time,limit,mid)
    
    return answer