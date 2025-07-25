
def solution(points, routes):
    # n개의 포인트 서로 다른 번호, 
    # 운송경로 m개 
    # 로봇 x대, 0초 동시 출발 
    # 최단경로로 이동하는데 여러가지면 r좌표가 변하는 이동을 c좌표보다 먼저 함 
    # 같은 좌표에 로봇 2대이상이면 충돌 - 위험한 상황이 총 몇번 일어나는지 

    
    # 이 문제의 핵심 아이디어 - 로봇이 각 초마다 어디에 있는가? 
    dic = {}
    
    for route in routes:
        time = 0
        
        cx,cy = points[route[0]-1]
        dic.setdefault((cx,cy), []).append(time)
        
        for i in range(1,len(route)):
            # route가 2개 이상 갈 수도 있으니 for문 사용 
            ex,ey = points[route[i]-1]
            
            step = 1 if cx < ex else -1
            while cx != ex:
                cx += step 
                time += 1
                dic.setdefault((cx,cy), []).append(time)
            
            step = 1 if cy < ey else -1 
            while cy != ey:
                cy += step
                time += 1
                dic.setdefault((cx,cy), []).append(time)
                
    answer = 0
    
    for times in dic.values():
        freq = dict()
        for t in times:
            freq[t] = freq.get(t,0)+1 
        
        for cnt in freq.values():
            if cnt > 1:
                answer += 1
            
        

    return answer