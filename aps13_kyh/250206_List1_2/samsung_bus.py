T = int(input())
for tc in (1, T + 1):
    n = int(input())
    bstop = [0] * 5001

    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b+1):
            bstop[i] += 1

    print(f"#{tc}", end=' ')
    p = int(input())
    for _ in range(p):
        c = int(input())
        print(f"{bstop[c]}", end=' ')








