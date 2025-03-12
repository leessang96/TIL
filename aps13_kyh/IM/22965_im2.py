T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    direction = [[0,1], [1,0], [0,-1], [-1,0]]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                for di, dj in direction:
                    for k in range(1, n):
                        ni, nj = i + di * k, j + dj * k

                        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
                            arr[ni][nj] += 1
                        else:
                            break
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                cnt += 1

    print(f"#{tc} {cnt}")