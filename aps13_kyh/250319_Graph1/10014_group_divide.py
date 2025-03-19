def find_set(i):
    while parents[i] != i:
        parents[i] = parents[parents[i]]
        i = parents[i]
    return i


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ranks[ref_x] < ranks[ref_y]:
        parents[ref_x] = ref_y
    elif ranks[ref_x] > ranks[ref_y]:
        parents[ref_y] = ref_x
    else:
        parents[ref_y] = ref_x
        ranks[ref_x] += 1


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    parents = [i for i in range(N + 1)]
    ranks = [0] * (N + 1)

    for i in range(0, M * 2, 2):
        union(arr[i], arr[i + 1])

    groups = set(find_set(i) for i in range(1, N+1))

    print(f"#{tc} {len(groups)}")
