T = int(input())
for tc in range(1, T+1):
    p, a, b = map(int, input().split())

    def binarySearch(p, key):
        left = 1
        right = p
        count = 0

        while left <= right:
            center = (left + right) // 2
            if center == key:
                return count
            elif center > key:
                right = center
                count += 1
            else:
                left = center
                count += 1

    count_a = binarySearch(p, a)
    count_b = binarySearch(p, b)

    if count_a < count_b:
        print(f"#{tc} A")
    elif count_a == count_b:
        print(f"#{tc} 0")
    else:
        print(f"#{tc} B")