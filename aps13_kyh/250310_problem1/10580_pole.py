# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())    # 전선의 개수
    arr = [[0] * 2 for _ in range(N)]
    cnt = 0
    i = 0

    for _ in range(N):
        A, B = map(int, input().split())    # A 고도, B 고도

        arr[i][0] = A
        arr[i][1] = B

        i += 1

    for i in range(N):
        for j in range(1+i, N):
            if arr[i][0] > arr[j][0] and arr[i][1] < arr[j][1]:
                cnt += 1
            elif arr[i][0] < arr[j][0] and arr[i][1] > arr[j][1]:
                cnt += 1

    print(f"#{tc} {cnt}")
