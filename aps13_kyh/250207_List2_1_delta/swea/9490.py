T = 1
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    max_v = 0
    for i in range(n):
        for j in range(m):
            s = arr[i][j]
            for d in range(4):
                ni = i + di[d]
                nj = j + dj[d]

                if 0<=ni<n and 0<=nj<m:
                    s += arr[i][j]
                    s += arr[ni][nj]
            if max_v < s:
                max_v = s

    print(s)