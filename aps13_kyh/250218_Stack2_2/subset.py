# def f(i, n):        # i 인덱스, n은 배열 크기
#     if i == n:
#         print(bit)
#         s = 0   # 부분집합의 합
#         for j in range(n):
#             if bit[j]:
#                 s += A[j]
#         print(s)
#
#     else:
#         bit[i] = 1  # bit[i] 를 1로 결정
#         f(i+1, n)   # bit[i+1] 결정하러 이동
#         bit[i] = 0
#         f(i+1, n)
#
#
# A = [1,2,3]
# bit = [0] * len(A)
# f(0, len(A))

# def f(i, n, s):        # i 인덱스, n은 배열 크기, i-1까지 결정한 원소의 합
#     if i == n:
#         print(bit, s)
#     else:
#         bit[i] = 1  # bit[i] 를 1로 결정
#         f(i+1, n, s + A[i])   # bit[i+1] 결정하러 이동
#         bit[i] = 0
#         f(i+1, n, s)
#
#
# A = [1,2,3]
# bit = [0] * len(A)
# f(0, len(A), 0)

# def f(i, n, s, t):
#     global cnt
#     cnt += 1
#     if s > t:           # 찾는 합보다 커지면 중지
#         return
#     if i == n:
#         if s == t:  # 찾는 값이면
#             print(bit, s)
#     else:
#         bit[i] = 1      # bit[i]를 1로 결정
#         f(i+1, n, s+ A[i], t)   #bit[i+1] 결정하러 이동
#         bit[i] = 0
#         f(i+1, n, s, t)
#
#
# A = [1,2,3,4,5,6,7,8,9,10]
# bit = [0] * len(A)
# cnt = 0
# f(0, len(A), 0, 2)
# print(cnt)


def f(i, n, s, t):
    global cnt
    cnt += 1
    if s == t:
        print(bit, s)
    elif s > t:
        return
    elif i == n:
        return
    else:
        bit[i] = 1      # bit[i]를 1로 결정
        f(i+1, n, s+ A[i], t)   #bit[i+1] 결정하러 이동
        bit[i] = 0
        f(i+1, n, s, t)


A = [1,2,3,4,5,6,7,8,9,10]
bit = [0] * len(A)
cnt = 0
f(0, len(A), 0, 2)
print(cnt)