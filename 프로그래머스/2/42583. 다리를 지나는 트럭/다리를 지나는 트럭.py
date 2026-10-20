from collections import deque

def solution(bridge_length, weight, truck_weights):
    trucks = deque(truck_weights)
    bridge = deque([0] * bridge_length) # [0,0]
    bridge_weight = 0 
    cnt = 0
    
    while trucks:
        left = bridge.popleft()
        
        if sum(bridge) + trucks[0] <= weight:
            truck = trucks.popleft()
            bridge.append(truck)
            bridge_weight += truck
            cnt += 1
        
        else:
            bridge.append(0)
            cnt += 1
            
    return cnt + bridge_length