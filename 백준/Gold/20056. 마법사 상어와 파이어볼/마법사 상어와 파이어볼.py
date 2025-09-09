import math
n,m,k = map(int,input().split())
board = [[[] for _ in range(n)] for _ in range(n)]
info = []

for _ in range(m):
    r,c,m,s,d = map(int,input().split())
    obj = [r-1,c-1,m,s,d]
    board[r-1][c-1].append(obj)
    info.append(obj)

dir = {0:(-1,0), 1:(-1,1), 2:(0,1), 3:(1,1), 4:(1,0), 5:(1,-1), 6:(0,-1), 7:(-1,-1)}


# 1단계
for _ in range(k):

    cnt = 0
    for _ in range(len(info)):
        obj = info.pop(0)               # 현재 파이어볼 꺼내기
        sx, sy = obj[0], obj[1]
        nd, ns = obj[4], obj[3]
        nx, ny = (sx + dir[nd][0] * ns) % n, (sy + dir[nd][1] * ns) % n

        board[sx][sy].remove(obj)       # 원래 칸에서 제거
        obj[0], obj[1] = nx, ny         # 좌표 갱신
        board[nx][ny].append(obj)       # 새 칸에 넣기
        info.append(obj)                # info 갱신

    
    new_info = []
    for i in range(n):
        for j in range(n):
            if len(board[i][j]) >= 2:   # 2개 이상일 때만 합치기
                l = len(board[i][j])
                m_sum = sum(f[2] for f in board[i][j])
                s_sum = sum(f[3] for f in board[i][j])
                dirs = [f[4] % 2 for f in board[i][j]]

                nm = m_sum // 5
                ns = s_sum // l
                board[i][j] = []        # 기존 파이어볼 제거

                if nm == 0:
                    continue

                if all(d == 0 for d in dirs) or all(d == 1 for d in dirs):
                    new_dirs = [0,2,4,6]
                else:
                    new_dirs = [1,3,5,7]

                for d in new_dirs:
                    new_obj = [i,j,nm,ns,d]
                    board[i][j].append(new_obj)
                    new_info.append(new_obj)
            elif len(board[i][j]) == 1: # 그대로 유지
                new_info.append(board[i][j][0])

    info = new_info[:]   # info 새로 갱신

res = sum(obj[2] for obj in info)
print(res)
        
    