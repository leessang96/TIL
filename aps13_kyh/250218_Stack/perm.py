def f(i, n, s):            # 크기가 n이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    global min_v
    global cnt
    cnt += 1
    if i == n:
        if min_v > s :
            min_v = s
    elif min_v < s: # 중간 합계가 최소합보다 크면
        return
    else:
        for j in range(i, n):
            p[i], p[j] = p[j], p[i]     # 자리교환
            f(i+1, n, s + arr[i][p[i]])   # i+1 자리 결정
            p[i], p[j] = p[j], p[i]     # 원상복구


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

p = [i for i in range(n)]   # p[i] : i에서 고른 열 번호
min_v = 10000
cnt = 0
f(0, n, 0)
print(min_v, cnt)

# p = [1,2,3,4,5]
# n = 5
# f(0, n)

# 어떤 문제에 활용하느냐?????
'''
주로 TSP 문제에 많음
집에서 출발해 1~10 도시를 돌 때의 최소비용은 얼마인가?
'''


