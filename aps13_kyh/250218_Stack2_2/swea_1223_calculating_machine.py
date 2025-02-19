T = 10
for tc in range(1, T + 1):
    answer = 0

    N = int(input())
    infix = input()

    postfix = ''
    stack = []

    # 후위 표기식 만들기
    for i in range(N):
        c = infix[i]

        if c == '+':
            while stack:
                postfix += stack.pop()
            stack.append(c)
        elif c == '*':
            while stack and stack[-1] == '*':
                postfix += stack.pop()
            stack.append(c)
        else:
            postfix += c

    while stack:
        postfix += stack.pop()

    # 후위 표기식 기반 계산하기
    for i in range(N):
        c = postfix[i]

        if c == '*':
            a = stack.pop()
            b = stack.pop()
            stack.append(a * b)
        elif c == '+':
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b)
        else:
            stack.append(int(c))

    answer = stack.pop()

    print(f'#{tc} {answer}')