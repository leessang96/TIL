# def f(change, N, M): # 이전까지의 교환횟수
#     global max_v
#
#     if change == N:  # 주어진 교환 횟수 사용
#         tmp = int(''.join(card))
#         if max_v < tmp:
#             max_v = tmp
#     else:
#         for i in range(M-1):
#             for j in range(i+1, M):
#                 card[i], card[j] = card[j], card[i]
#                 tmp = int(''.join(card))
#                 if tmp not in memo[change]:
#                     memo[change].append(tmp)
#                     f(change + 1, N, M)
#                 card[i], card[j] = card[j], card[i]
#
#
# T = int(input())
# for tc in range(1, T+1):
#     num, N = input().split()
#     card = list(num)
#     N = int(N)
#     M = len(card)
#     max_v = 0
#     memo = [[] for _ in range(N)]
#     f(0, N, M)
#     print(f"#{tc} {max_v}")

# def f(i, M, N):     # i 카드 위치, M 카드 수, N 남은교환횟수
#     global max_v, max_c # max_c는 max_v를 찾았을 때의 최소 교환횟수 max_c
#     if i == M or N == 0:
#         tmp = int(''.join(card))
#         if max_v <= tmp:
#             max_v = tmp
#             if max_c[max_v] > N:   # 최댓값을 찾을 때의 최소 교환 횟수
#                 max_c[max_v] = N
#     else:
#         for j in range(M):
#             if i != j:      # 교환
#                 card[i], card[j] = card[j], card[i]
#                 f(i+1, M, N-1)
#                 card[i], card[j] = card[j], card[i]
#             else:   # i == j 교환 횟수를 다른 자리에서 사용하도록 넘겨줌
#                 f(i+1, M, N)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     num, N = input().split()
#     card = list(num)
#     N = int(N)
#     M = len(card)
#     max_v = 0
#     max_c = [0] * (10**M)
#     f(0, N, M)
#     if max_c[max_v] % 2:        # 남은 교환횟수가 홀수번인 경우
#         n1 = max_v % 10         # 1의 자리
#         n10 = max_v % 100 // 10 # 10의 자릿수
#
#     print(f"#{tc} {max_v}")


T = int(input())
# 재귀 함수
# 교환 횟수 : k
def solve(k):
    global max_price

    # 0. 가지치기
    if (k, "".join(numbers)) in visited:
        # k번 교환해서 numbers 문자열을 이전에 만든적이 있다면 더이상 교환 진행x
        return


    # 1. 종료 조건
    if k == cnt:
        # cnt번 다 바꾸면 상금중에 최댓값 계산
        # ['1','2','3'] => '123'
        # ''.join(['1','2','3'])
        price = int("".join(numbers))
        max_price = max(price, max_price)
        return

    # 2. 재귀 호출
    # 자리 교환 한번 하고
    # solve(k+1)


    # 자리 교환은 어떻게 할까??
    # 자리교환할 위치 두개 앞쪽, 뒷쪽 위치
    # 자리를 교환할 두개의 위치를 정해줘야 한다
    # 앞쪽 위치 i, 뒤쪽 위치 j
    # i : 바꿀 숫자 중에 앞쪽 인덱스 (N-1 까지인 이유는 최소 뒤에 1개 남겨둬야함)
    # j : 바꿀 숫자 중에 뒤쪽 인덱스 (i+1 부터 시작)
    for i in range(N - 1):
        for j in range(i + 1, N):
            # i번째와 j번째 교환 하고
            numbers[i], numbers[j] = numbers[j], numbers[i]
            # 다음 교환 횟수 채우러 재귀 호출
            solve(k + 1)
            # 원상복구
            numbers[i], numbers[j] = numbers[j], numbers[i]


for tc in range(1, T + 1):
    numbers, cnt = input().split()

    # cnt는 숫자니까 숫자로 바꿔 주고
    # 반드시 자리 교환을 cnt 번 해야한다.
    cnt = int(cnt)

    # 문자열을 불변이니까 자리를 교환 가능한 리스트로 바꾸자.
    numbers = list(numbers)

    # 자리 교환 어디랑 어디를 교환 할건지
    # 교환 범위 (i =0, j=1) 0 <= i,j < len(numbers)
    N = len(numbers)

    max_price = 0
    # 중복체크용 세트
    # 세트 안에는 (교환횟수, 해당교환횟수에서 만든 문자열)
    # 3번의 교환을 통해 "12345" 를 만들었다면
    # 이후에 다른 방법으로 3번 교환해서 "12345" 가 만들어지면 더 교환해볼 필요가 없다!!
    visited = set()

    # 자리교환 0번 한 상태에서 시작!
    solve(0)

    print(f"#{tc} {max_price}")