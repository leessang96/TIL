def pre_order(n):
    global cnt
    if n:
        cnt += 1
        pre_order(left[n])
        pre_order(right[n])
    return cnt

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())        # E = 간선의 개수, N = 노드 번호
    arr = list(map(int, input().split()))   # 2 1 2 5 1 6 5 3 6 4

    left = [0] * (E+2)
    right = [0] * (E+2)
    par = [0] * (E+2)

    for i in range(E):  # 0,1,2,3,4
        p, c = arr[i*2], arr[i*2+1]
        par[c] = p

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    cnt = 0
    pre_order(N)
    print(f"#{tc} {cnt}")