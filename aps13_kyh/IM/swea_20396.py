T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    for _ in range(m):
        i, j = map(int, input().split())

        for s in range(i, i+j-1):
            if s < len(arr):
                if arr[s] != arr[i-1]:
                    arr[s] = arr[i-1]

    print(f'#{tc}', *arr)