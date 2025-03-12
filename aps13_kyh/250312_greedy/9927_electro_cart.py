
# 1. 모든 경로를 다 확인하고 값을 비교하는 방법
# def cost(N):
#     total = 0
#     for i in range(1, N):
#         total += arr[p[i-1]][p[i]]
#     total += arr[p[N-1]][0]
#     return total
#
#
# def f(i, N):
#     global min_e
#     if i == N:
#         tmp = cost(N)
#         if min_e > tmp:
#             min_e = tmp
#     else:
#         for j in range(N):
#             if used[j] == 0:
#                 used[j] = 1
#                 p[i] = j
#                 f(i+1, N)
#                 used[j] = 0
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#
#     used = [0] * N
#     p = [0] * N         # 사무실 0번, 관리구역 1~N-1 번
#     p[0] = 0
#     used[0] = 1
#     min_e = 100000      # 두 구역사이 최대 100, 최대 10번 이동
#     f(1, N)
#
#     print(f"#{tc} {min_e}")

def f(i, N, s): # i구역까지의 배터리 소모 s
    global min_e
    if i == N:
        tmp = s + arr[p[N-1]][0]
        if min_e > tmp:
            min_e = tmp
    else:
        for j in range(N):
            if used[j] == 0:
                used[j] = 1
                p[i] = j
                f(i+1, N, s+arr[p[i-1]][j])
                used[j] = 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    used = [0] * N
    p = [0] * N         # 사무실 0번, 관리구역 1~N-1 번
    p[0] = 0
    used[0] = 1
    min_e = 100000      # 두 구역사이 최대 100, 최대 10번 이동
    f(1, N, 0)

    print(f"#{tc} {min_e}")