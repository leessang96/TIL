T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    dx = [-1, 1]
    for _ in range(m):
        i, j = map(int, input().split())
        i -= 1
        for k in range(1, j+1):
            l = i + dx[0] * k
            r = i + dx[1] * k

            if l < 0 or r >= n:
                continue
            if arr[l] == arr[r]:
                arr[l] = 1 - arr[l]
                arr[r] = 1 - arr[r]

    print(f'#{tc}', *arr)