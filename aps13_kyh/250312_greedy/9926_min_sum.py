def f(i, j):
    global start, min_v
    if min_v < start:
        return

    if i == N-1 and j == N-1:
        min_v = start
        return

    for di, dj in direction:
        ni = i + di
        nj = j + dj

        if 0 <= ni < N and 0 <= nj < N:
            start += arr[ni][nj]
            f(ni, nj)
            start -= arr[ni][nj]


direction = [[0,1], [1,0]]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    start = arr[0][0]
    min_v = 200
    f(0, 0)
    print(f"#{tc} {min_v}")


# def f(i, j, s):     # i,j칸에 진입, 지나온칸의 합계 s
#     global min_v
#
#     if i == N-1 and j == N-1:   # 맨 오른쪽 아래 칸에 도착한 경우
#         if min_v > s + arr[i][j]:
#             min_v = s + arr[i][j]
#     else:
#         if i+1 < N:
#             f(i+1, j, s+arr[i][j])
#         if j+1 < N:
#             f(i, j+1, s+arr[i][j])
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     min_v = 1000
#     f(0, 0, 0)
#
#     print(f"#{tc} {min_v}")

# def f(i, j):
#     if i == N-1 and j == N-1:   # 목적지 도착
#         return arr[i][j]
#     if i == N or j == N:    # 벗어나면
#         return 1000         # 합계가 작은 쪽을 택하므로 무시되는 값
#     else:
#         r1 = f(i+1, j)  # 아래 방향으로 이동했을 때 지나는 칸들의 합계
#         r2 = f(i, j+1)  # 오른쪽 방향으로 이동했을 때 지나는 칸들의 합계
#         return min(r1, r2) + arr[i][j]
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     min_v = f(0,0)
#     print(f"#{tc} {min_v}")


# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     dp = [[0] * N for _ in range(N)]
#     dp[0][0] = arr[0][0]
#     for i in range(1, N):
#         dp[0][i] = dp[0][i-1] + arr[0][i]
#         dp[i][0] = dp[i-1][0] + arr[i][0]
#
#     for i in range(1, N):
#         for j in range(1, N):
#             dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + arr[i][j]
#
#     print(f"#{tc} {dp[N-1][N-1]}")