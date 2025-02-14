T = 1
for tc in range(1, T+1):
    n = int(input())

    arr = [[0 for _ in range(n)] for _ in range(n)]
    i = 0
    j = 0
    dir = 0
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    for k in range(1, n*n+1):
        arr[i][j] = k

        ni = i + di[dir]
        nj = j + dj[dir]

        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] == 0:
            i, j = ni, nj
        else:
            dir = (dir+1) % 4
            i, j = i+di[dir], j+dj[dir]

    print(f'#{tc}')
    for x in arr:
        print(*x)