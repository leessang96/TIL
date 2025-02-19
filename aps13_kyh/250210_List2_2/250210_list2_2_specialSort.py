T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    for i in range(n-1):
        min_i = i
        for j in range(i+1, n):
            if i % 2 == 0:
                if arr[min_i] < arr[j]:
                    min_i = j
            else:
                if arr[min_i] > arr[j]:
                    min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]

    print(f"#{tc}", *arr[0:10])