T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [[0] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == 0 or i == j:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]


    print(arr)