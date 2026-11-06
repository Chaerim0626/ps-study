from collections import deque
def solution(places):
    answer = []
    # P 응시자, O 빈 테이블, X 파티션 
    # P에서 출발해서, BFS 돌려서 O면 가는데 거리가 2 넘으면 return 0 
    # X 로 뚫려있으면 못감 
    
    def bfs(sx,sy,graph,visited):
        result = 1
        dir = [(0,1),(0,-1),(1,0),(-1,0)]
        dq = deque([(sx,sy,0)])
        visited[sx][sy] = 1
        
        while dq:
            cx,cy,cnt = dq.popleft()
            if cnt == 1 or cnt == 2:
                if graph[cx][cy] == 'P':
                    return 0 
            
            for dx,dy in dir:
                nx,ny = dx+cx, dy+cy 
                if 0 <= nx < 5 and 0 <= ny < 5:
                    if not visited[nx][ny] and graph[nx][ny] != 'X':
                        dq.append((nx,ny,cnt+1))
                        visited[nx][ny] = 1 
     
        return 1
    
    def solve(graph):

        for i in range(5):
            for j in range(5):
                if graph[i][j] == 'P':
                    visited = [[0] * 5 for _ in range(5)]
                    if not bfs(i,j,graph,visited):
                        return 0

        return 1
                    
    for i in range(5):
        res = solve(places[i])
        answer.append(res)
        print(res)
    return answer