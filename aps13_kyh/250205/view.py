T = 3
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    answer = 0
    for i in range(2, n-2):
        max_h = 0
        l1 = arr[i-2]
        l2 = arr[i-1]
        r1 = arr[i+1]
        r2 = arr[i+2]

        height = [l1, l2, r1, r2]
        for j in range(len(height)):
            if max_h < height[j]:
                max_h = height[j]

        if max_h > arr[i]:
            continue
        else:
            answer += arr[i] - max_h

    print(f"#{tc} {answer}")