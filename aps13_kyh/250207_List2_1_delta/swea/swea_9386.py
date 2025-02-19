T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input()))

    cnt = 0
    max_v = 0
    for i in range(n):
        if arr[i] == 1:
            cnt += 1
        else:
            cnt = 0

        if max_v < cnt:
            max_v = cnt

    print(f'#{tc} {max_v}')