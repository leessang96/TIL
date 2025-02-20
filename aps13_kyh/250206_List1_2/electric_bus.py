# T = int(input())
# for tc in range(1, T + 1):
#     # 최대한 이동할 수 있는 정류장 수 k
#     # 종점인 n, 충전기가 설치된 m개의 정류장
#     k, n, m = map(int, input().split())
#     charger = [0] + list(map(int, input().split())) + [n]
#
#     count = 0  # 충전 횟수
#     last = 0  # 마지막 충전 위치
#     for i in range(1, m + 2):  # 충전기 사이 거리
#         if charger[i - 1] + k < charger[i]:  # 운행 불가
#             count = 0
#             break
#         elif last + k < charger[i]:  # 마지막 충전 위치에서 올 수 없으면
#             last = charger[i - 1]
#             count += 1
#     print(f"#{tc} {count}")



# 좀 어려운 문제임, 실제 코테와 비슷
T = int(input())
for tc in range(1, T+1):
    k, n, m = map(int, input().split())
    arr = [0] + list(map(int, input().split())) + [n]

    count = 0    # 충전 count
    last = 0     # 마지막 충전 위치
    for i in range(1, m+2):
        if arr[i - 1] + k < arr[i]:
            count = 0
            break
        elif last + k < arr[i]:
            last = arr[i - 1]
            count += 1
    print(f'#{tc} {count}')
