# T = int(input())
# for tc in range(1, T + 1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#
#     max_idx = 0
#     min_idx = 0
#
#     for i in range(N):
#         if arr[max_idx] <= arr[i]:       # 가장 큰 수가 여러 개이면 마지막으로 나오는 위치
#             max_idx = i
#         if arr[min_idx] > arr[i]:
#             min_idx = i
#     # print(f'#{tc} {abs(min_idx - max_idx)}')      # 내장함수 사용 시
#
#     # 내장함수 사용 x
#     ans = max_idx - min_idx
#     if ans < 0:
#         ans *= -1
#
#     ans = max_idx - min_idx if max_idx > min_idx else min_idx - max_idx
#     print(f'#{tc} {ans}')


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = list(map(int, input().split()))

    min_i = 0
    max_i = 0

    for i in range(n):
        if arr[min_i] > arr[i]:
            min_i = i
        if  arr[max_i] <= arr[i]:
            max_i = i

    answer = max_i - min_i if max_i > min_i else min_i - max_i
    print(f'#{tc} {answer}')