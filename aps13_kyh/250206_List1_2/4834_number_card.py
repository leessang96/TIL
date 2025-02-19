T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))

    count = [0] * 10        # 숫자는 0이상 9이하

    for i in range(N):      # for x in arr:
        count[arr[i]] += 1  # count[x] += 1

    # count의 최댓값(최대 개수) 인덱스 찾기
    max_idx = 0         # 첫 원소를 최댓값으로 지정
    for i in range(1, 10):  # 범위 주의
        if count[max_idx] <= count[i]:      # <면 최댓값 중 가장 왼쪽
            # <=이면 오른쪽 애로 갱신되는 것
            max_idx = 1
    print(f'#{tc} {max_idx} {count[max_idx]}')
