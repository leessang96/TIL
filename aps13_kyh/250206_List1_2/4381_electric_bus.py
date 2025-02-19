T = int(input())
for tc in range(1, T + 1):
    # 최대한 이동할 수 있는 정류장 수: K
    # 종점인 N, 충전기가 설치된 M개의 정류장
    K, N, M = map(int, input().split())
    charger = [0] + list(map(int, input().split())) + [N]
    # 이러면 왼쪽에 0, 오른쪽에 N 요소를 추가한 상태

    ans = 0         # 충전횟수
    last = 0        # 마지막 충전 위치
    for i in range(1, M + 2):   # M + 2는 마지막 인덱스, 충전기 사이 거리
        if charger[i - 1] + K < charger[i]:  # 운행불가
            ans = 0
            break
        elif last + K < charger[i]:        # 마지막 충전 위치에서 올 수 없으면
            last = charger[i - 1]
            ans += 1
    print(f'#{tc} {ans}')

