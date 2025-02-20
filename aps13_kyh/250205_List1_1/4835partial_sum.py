# T = int(input())
#
# for tc in range(1, T + 1):      # 케이스 별로 처리
#     sum_list = []
#     N, M = map(int, input().split())
#     arr = [map(int, input().split())]
#     # print(tc)
#     # print(N, M)
#
#     min_sum = 2         # M의 최소: 2, M의 요소인 a의 최소: 1
#     # 이런 경우 보통은 0으로 함. 그게 눈에 확 들어와서
#     max_sum = 1000000   # 10000 * 100
#     for i in range(N - M + 1):
#         sum = 0
#         for j in range(M):
#             sum += arr[i + j]


T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    min_v = 100000
    max_v = 0
    for i in range(n - m + 1):
        s = 0
        for j in range(m):
            s += arr[i+j]
        if max_v < s:
            max_v = s
        if min_v > s:
            min_v = s

    print(f'#{tc} {max_v - min_v}')