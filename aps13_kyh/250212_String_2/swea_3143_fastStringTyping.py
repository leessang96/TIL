T = int(input())
for tc in range(1, T+1):
    a, b = input().split()  # a = 전체 문자열 / b = 찾을 문자열

    n = len(a)      # 전체 문자열의 길이 sasasaaaa
    m = len(b)      # 찾을 문자열의 길이 sasa

    cnt = 0
    i, j = 0, 0
    while i < n:
        if a[i] == b[j]:
            if j == m-1:
                cnt += 1
                i += 1
                j = 0
            else:
                i += 1
                j += 1
        else:
            i = i - j + 1
            j = 0

    cnt = n - cnt * m + cnt

    print(f"#{tc} {cnt}")