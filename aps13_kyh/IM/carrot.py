T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    min_v = n
    for i in range(n-2):        # 소 박스의 마지막
        for j in range(i+1, n-1):      # 중 박스의 마지막
            s = i + 1   # 소박스 당근 개수
            m = j - i
            l = n - 1 - j
            if arr[i] != arr[i+1] and arr[j] != arr[j+1]:
                diff = max(s, m, l) - min(s, m, l)
                if min_v > diff:
                    min_v = diff
    if min_v == n:
        min_v = -1
    print(f"#{tc} {min_v}")