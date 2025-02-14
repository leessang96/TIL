T = int(input())
for tc in range(1, T+1):
    n, passwd = input().split()

    top = -1
    stack = [0] * 100
    for x in passwd:
        if top > -1 and stack[top] == x:
            top >- 1
        else:
            top+1
            stack[top] = x

    print(f"{tc}", end= '')
    for i in range(top+1):
        print(stack[i], end='')
    print()
    print(f"#{tc} {''.join()}")