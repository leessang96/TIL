T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    min_v = 200
    min_i = 0
    for i in range(n-1):            # i 첫 일꾼의 수확 범위
        if min_v > abs(sum(arr[:i+1]) - sum(arr[i+1:])):
            min_v = abs(sum(arr[:i+1]) - sum(arr[i+1:]))
            min_i = i
    print(f"#{tc} {min_i+1} {min_v}")