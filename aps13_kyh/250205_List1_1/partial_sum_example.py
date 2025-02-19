T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    # N개의 정수가 들어있는 배열에서 이웃한 M개의 합, 최댓값 - 최솟값
    max_v = 0   # 입력 조건이 1 이상이므로(최솟값 이하로 초기화)
    min_v = 1000000     # 10000 이하 100개, 가능한 최대값 이상으로 초기화
    # 종종 float의 최대범위로 min/max 사용하는 사람 있는데, 그러지 마세요
    # 그건 속도도 엄청 느려지게 만들고, 문제를 제대로 이해하지 못했다는 이야기가 됨
    for i in range(N - M + 1):  # 이웃한 M개의 시작 인덱스
        s = 0
        for j in range(M):      # 이웃한 m개 내부 순서 [i + j], in range(i, i + M) -> [j]
            s += arr[i + j]
        if max_v < s:
            max_v = s
        if min_v > s:
            min_v = s
    print(f'#{tc} {max_v - min_v}')

    # 이게 디지털 필터링의 기본. noise canceling의 기본임
    # 음성: 1차원, ~~: 2차원? 음성이 2차원인가?