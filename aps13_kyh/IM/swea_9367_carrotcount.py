T = int(input())
for tc in range(1, T+1):
    n = int(input())
    c = list(map(int, input().split()))

    max_v = 1
    cnt = 1
    for i in range(1, n):
        if c[i-1] < c[i]:
            cnt += 1
            if max_v < cnt:
                max_v = cnt
        else:
            cnt = 1

    print(f"#{tc} {max_v}")