T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    direction = [[0,1], [1,0], [0,-1], [-1,0]]
    max_v = 0
    for i in range(n):
        for j in range(m):
            s = arr[i][j]
            for di, dj in direction:
                for c in range(1, arr[i][j] + 1):
                    ni = i + di * c
                    nj = j + dj * c

                    if 0<=ni<n and 0<=nj<m:
                        s += arr[ni][nj]
            if max_v < s:
                max_v = s

    print(max_v)