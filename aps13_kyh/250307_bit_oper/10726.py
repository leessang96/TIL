import sys
sys.stdin = open("input.txt", "r")

# M의 우측 N개를 확인할 예정
# def solution():
#     target = M
#     # N 번 확인
#     for i in range(N):
#         # 맨 우측 비트가 1인지 체크
#         # 0x1, 0b1, 1 다 사용가능
#         # - 비트 연산이라는 것을 명시하기 위해 사용
#         if target & 0x1 == 0:
#             return False
#         # 맨 추윽 비트를 삭제
#         target >>= 1
#     return True

# 단순하게 하는 방법
def solution():
    # N 개의 1을 구함
    mask = (1 << N) - 1
    result = (M & mask) == mask
    return result

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    answer = solution()
    print(answer)