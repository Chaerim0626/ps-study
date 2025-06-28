import sys
input = sys.stdin.readline 
sys.setrecursionlimit(10**5)

R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]

ans = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(board, v, visited, depth):
    global ans

    x, y = v
    stack = set()
    stack.add((x, y, visited + board[x][y], depth))

    while stack:
        nx, ny, nowvisited, nowdepth = stack.pop()
        ans = max(ans, nowdepth)
        for i in range(4):
            newx = nx + dx[i]
            newy = ny + dy[i]
            if 0 <= newx < R and 0 <= newy < C and board[newx][newy] not in nowvisited:
                stack.add((newx, newy, nowvisited + board[newx][newy], nowdepth + 1))
    return

dfs(board, (0, 0), '', 1)

print(ans)