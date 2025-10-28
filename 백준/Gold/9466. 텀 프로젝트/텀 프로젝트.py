import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

def dfs(x):
    global cycle_count
    visited[x] = 1
    nxt = nums[x]

    if not visited[nxt]:      # 아직 방문 안 했으면 계속 DFS
        dfs(nxt)
    else:
        if not done[nxt]:     # ✅ 아직 처리 완료 안 되었으면 사이클
            cur = nxt
            while True:
                cycle_count += 1   # ✅ 사이클 노드만 count
                cur = nums[cur]
                if cur == nxt:
                    break

    done[x] = 1  # ✅ 처리 완료 표시

t = int(input())
for _ in range(t):
    n = int(input())
    nums = [0] + list(map(int, input().split()))

    visited = [0] * (n+1)
    done = [0] * (n+1)
    cycle_count = 0

    # 1) 자기 자신 루프 먼저 처리
    for i in range(1, n+1):
        if nums[i] == i:
            cycle_count += 1
            done[i] = 1
            visited[i] = 1

    # 2 ) 그 외 DFS 로 사이클만 찾기
    for i in range(1, n+1):
        if not visited[i]:
            dfs(i)

    # 팀 못 이루는 사람 출력
    print(n - cycle_count)
