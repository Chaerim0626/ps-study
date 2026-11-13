from collections import defaultdict

def solution(tickets):
    answer = []
    n = len(tickets) + 1
    visited = [False] * len(tickets) # i번째 '티켓'을 썼는지
    tickets.sort()     
    
    def dfs(start,path):
        if len(path) == n:
            answer.append(path)
            return  
        
        for i,ticket in enumerate(tickets):
            if not visited[i] and ticket[0] == start:
                visited[i] = True 
                dfs(ticket[1],path+[ticket[1]])
                visited[i] = False

    dfs('ICN',['ICN'])
    answer.sort()
    return answer[0]