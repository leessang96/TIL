T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[0] * 10 for _ in range(10)]

    for i in range(10):
        for j in range(i + 1):
            if j == 0 or i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]


    print(f"#{tc}")
    for i in range(n):
        print(*arr[i][:i+1])
