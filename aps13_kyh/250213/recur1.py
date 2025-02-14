# def f(i, n):
#     if i == n:
#         return
#     else:
#         print(A[i])
#         f(i+1, n)
#
# A = [1,2,3]
# f(0, 3)

def f(i, n, val):
    if i == n:
        return 0
    elif arr[i] == val:
        return 1
    else:
        return f(i+1, n, v)


arr = [1,2,3,4]
v = 3
print(f(0, len(arr), v))