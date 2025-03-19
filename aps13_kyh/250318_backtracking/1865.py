def dfs(i, total):
    global answer
    if total <= answer:
        return

    if i == N:
        answer = max(answer, total)
        return

    for j in range(N):
        if j not in path:
            path.append(j)
            dfs(i + 1, total * (arr[i][j] / 100))
            path.pop()


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    path = []
    answer = 0
    dfs(0, 1)
    result = round(answer * 100, 6)
    print(f"#{tc} {result:.6f}")