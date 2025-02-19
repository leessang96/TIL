# T = int(input())  # 테스트케이스 개수
#
# # tc = test case
# for tc in range(1, T + 1):  # 케이스 별로 처리
#     N = int(input())    # 케이스 별 입력 개수
#     arr = list(map(int, input().split()))
#
#     max_v = arr[0]      # 첫 원소를 최댓값으로 가정
#     min_v = arr[0]      # 첫 원소를 최솟값으로 가정
#
#     for i in range(N):
#         if max_v < arr[i]:
#             max_v = arr[i]
#         if min_v > arr[i]:
#             min_v = arr[i]
#
#     print(f'#{tc} {max_v - min_v}')
#     # 출력 시, #과 test case 사이, 아랫 줄과의 사이(깔끔하게 보이기 위해)도 똑같이 나와야 정답임
#     # tc 우측에 스페이스 들어가는건 상관 x
#
#     # 꿀팁: SWEA 입력을 긁어서 메모장으로 -> 마지막에 enter 추가
#     # 그러면, 엔터 따로 안쳐도 알아서 실행됨


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split()))

    min_v = a[0]
    max_v = a[0]
    for i in range(n):
        if max_v < a[i]:
            max_v = a[i]
        if min_v > a[i]:
            min_v = a[i]

    print(f"#{tc} {max_v - min_v}")