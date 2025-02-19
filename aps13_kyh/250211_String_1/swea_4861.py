T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())        # n = 크기 , m = 길이
    arr = [input() for _ in range(n)]   # n * n 크기의 글자판

    str1 = ""
    for i in range(n):
        for j in range(n - m + 1):
            for c in range(n // 2):
                if arr[i][j+c] != arr[i][j+m-1-c]:
                    break
            else:
                str1 = arr[i][j:m+j]

    for i in range(n):
        for j in range(n - m + 1):
            for c in range(n // 2):
                if arr[j+c][i] != arr[j+m-1-c][i]:
                    break
            else:
                for k in range(j, j+m):
                    str1 += arr[k][i]

    print(f"#{tc} {str1}")