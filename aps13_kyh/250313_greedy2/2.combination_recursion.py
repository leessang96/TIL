# arr = ['a', 'b', 'c', 'd', 'e']
# n = 3
# path = []
#
#
# # 5명 중 3명을 뽑는 문제
# def recur(cnt, start):
#     if cnt == n:
#         print(*path)
#         return
#
#     # 5명을 고려해야 한다.
#     # for i in range(이전에 뽑았던 인덱스 + 1 부터, len(arr)):
#     for i in range(start, len(arr)):
#         path.append(arr[i])
#         # i : i번째를 뽑겠다.
#         # i + 1을 매개변수로 전달: 다음 재귀 부터는 i+1 부터 고려
#         recur(cnt + 1, i + 1)
#         path.pop()
#
#
# recur(0, 0)

# 주사위 3개를 던져 나올 수 있는 모든 조합을 출력
# level : 주사위 3개를 던졌을 때
# branch : 1~6 숫자
n = 3
path = []


def recur(cnt, start):
    if cnt == n:
        print(path)
        return

    for i in range(start, 7):
        path.append(i)
        recur(cnt + 1, i)
        path.pop()


recur(0, 1)