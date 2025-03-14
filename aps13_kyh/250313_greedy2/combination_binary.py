# arr = ['A', 'B', 'C']
# n = len(arr)
#
#
# def get_sub(tar):
#     print(f'target = {tar}', end=' / ')
#     for i in range(n):
#         # 각각 원소가 포함되어 있는지 확인
#         if tar & 0x1:
#             print(arr[i], end='')
#         tar >>= 1       # 맨 우측 비트를 삭제한다
#                         # == 다음 원소를 확인하겠다.
#
#
# # 전체 부분집합을 확인해야한다.
# for target in range(1 << n):
#     get_sub(target)
#     print()


arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)

# 1인 bit 수를 반환하는 함수
def get_count(tar):
    cnt = 0
    for i in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1
    return cnt


# 모든 부분 집합 중 원소의 수가 2개 이상인 집합의 수
answer = 0
# 전체 부분집합을 확인해야한다.
for target in range(1 << n):
    if get_count(target) >= 2:
        answer += 1

print(answer)