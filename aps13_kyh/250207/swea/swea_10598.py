T = int(input())
for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = [x for x in range(1, 13)]
    result = 0
    for i in range(1 << 12):
        part = []
        sum_part = 0
        for j in range(12):
            if i & (i << j):
                part.append(arr[j])
                sum_part += arr[j]
        if len(part) == n:
            if sum_part == k:
                result += 1

    print(f'#{tc} {result}')