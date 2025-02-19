T = int(input())
for tc in range(1, T+1):
    susik = input().split()
    top = -1
    stack = [0] * 257

    for i in susik:
        if i not in '+-/*.':
            top += 1
            stack[top] = int(i)
        else:
            op2 = stack[top]
            top -= 1
            op1 = stack[top]
            top -= 1
            if i == '+':
                top += 1
                stack[top] = op1 + op2
            elif i == '-':
                top += 1
                stack[top] = op1 - op2
            elif i == '/':
                top += 1
                stack[top] = op1 // op2
            elif i == '*':
                top += 1
                stack[top] = op1 * op2
            elif i == '.':
                if top == -2:
                    print(f'#{tc} {stack[0]}')
                else:
                    print(f'#{tc} error')
