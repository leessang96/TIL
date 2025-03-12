T = int(input())
for tc in range(1, T+1):
    x1, y1, p1, q1 = map(int, input().split())
    x2, y2, p2, q2 = map(int, input().split())

    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        print(f"#{tc} 4")
    elif x1 == p2 or x2 == p1:
        if q1 == y2 or x2 == p1:
            print(f"#{tc} 3")
        else:
            print(f"#{tc} 2")
    elif q1 == y2 or q2 == y1:
        print(f"#{tc} 2")
    else:
        print(f"#{tc} 1")

