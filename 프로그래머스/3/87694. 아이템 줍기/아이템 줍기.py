from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    k = 2 # 배율
    board = [[0] * 102 for _ in range(102)] # board[x][y]

    # 1. 테두리 포함 전체를 1로 칠하기
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * k, y1 * k, x2 * k, y2 * k
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                board[x][y] = 1

    # 2. 안쪽(테두리 제외)을 0으로 지우기
    for x1, y1, x2, y2 in rectangle:
        x1, y1, x2, y2 = x1 * k, y1 * k, x2 * k, y2 * k
        for x in range(x1 + 1, x2):
            for y in range(y1 + 1, y2):
                board[x][y] = 0

    
    dirs = [(0,1), (0,-1), (1,0), (-1,0)]
    def bfs(sx, sy):
        visited = [[False] * 102 for _ in range(102)]
        visited[sx][sy] = True
        dq = deque([(sx, sy, 0)])

        while dq:
            x, y, cnt = dq.popleft()
            if x == itemX *2 and y == itemY * 2:
                return cnt // 2
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < 102 and 0 <= ny < 102 and not visited[nx][ny] and board[nx][ny] == 1:
                    visited[nx][ny] = True
                    dq.append((nx, ny, cnt + 1))
        return -1
    
    return bfs(characterX*2, characterY*2)