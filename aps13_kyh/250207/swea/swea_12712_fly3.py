T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    max_v = 0
    # 십자
    for i in range(n):
        for j in range(n):
            s = arr[i][j]
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
                for k in range(1, m):
                    ni = i + di * k
                    nj = j + dj * k

                    if 0 <= ni < n and 0 <= nj < n:
                        s += arr[ni][nj]
            if max_v < s:
                max_v = s
    # 대각
    for i in range(n):
        for j in range(n):
            s = arr[i][j]
            for di, dj in [[1,1], [1,-1], [-1,-1], [-1, 1]]:
                for k in range(1, m):
                    ni = i + di * k
                    nj = j + dj * k

                    if 0 <= ni < n and 0 <= nj < n:
                        s += arr[ni][nj]
            if max_v < s:
                max_v = s

    print(f"#{tc} {max_v}")