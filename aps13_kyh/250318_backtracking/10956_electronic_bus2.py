def f(i, n, e, c):
    global min_c
    if i == n:
        if min_c > c:
            min_c = c
    elif min_c <= c:
        return
    else:
        f(i+1, n, arr[i-1]-1, c+1)
        if e > 0:
            f(i+1, n, e-1, c)


T = int(input())
for tc in range(1, T+1):
    N, *arr = map(int, input().split())
    min_c = N
    f(2, N, arr[0]-1, 0)
    print(f"#{tc} {min_c}")