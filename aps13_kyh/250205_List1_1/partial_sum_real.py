T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # N개의 정수가 들어있는 배열에서 이웃한 M개의 합, 최댓값 - 최솟값
    max_v = 0   # 입력 조건이 1 이상이므로(최솟값 이하로 초기화)
    min_v = 1000000     # 10000 이하 100개, 가능한 최대값 이상으로 초기화

    # 첫 구간의 합
    s = 0
    for i in range(M):
        s += arr[i]

    max_v = s   # 첫 구간합으로 초기화
    min_v = s

    for i in range(N - M):      # 다음 구간에서 뺄 원소
        s -= arr[i]
        s += arr[i + M]
        if max_v < s:
            max_v = s
        if min_v > s:
            min_v = s
# 2중 for문은 보통 n^2으로 표현됨. 구간이 점점 줄어들지만, n번일어나서 n^2으로 보통 표현
    print(f'#{tc} {max_v - min_v}')