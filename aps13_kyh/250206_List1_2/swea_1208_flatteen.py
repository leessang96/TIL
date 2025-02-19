T = 10
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    for _ in range(n):
        max_i = 0
        min_i = 0
        for i in range(100):
            if arr[i] > arr[max_i]:
                max_i = i
            if arr[i] < arr[min_i]:
                min_i = i

        arr[max_i] -= 1
        arr[min_i] += 1

    # 덤프 끝나고 한번 더 찾아서
    max_i = 0
    min_i = 0
    for i in range(100):
        if arr[i] > arr[max_i]:
            max_i = i
        if arr[i] < arr[min_i]:
            min_i = i

    print(f"#{tc} {arr[max_i] - arr[min_i]}")