def dfs(i):
    global min_cost, s

    if i == N:
        if min_cost > s:
            min_cost = s
        return
    elif min_cost <= s:
        return
    else:
        for j in range(N):
            if visited[j] == 0:
                visited[j] = 1
                s += arr[i][j]
                dfs(i + 1)
                visited[j] = 0
                s -= arr[i][j]


T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 제품 개수 N
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    s = 0
    min_cost = 100000

    dfs(0)
    print(f"#{tc} {min_cost}")