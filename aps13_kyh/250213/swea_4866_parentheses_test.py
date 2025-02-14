'''
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())
'''
T = int(input())
for tc in range(1, T+1):

    # 1218 과롷 짝짓기 참고...
    txt = input()

    top = -1
    stack = [0] * 100

    ans = 1  # 짝이 맞다고 가정
    for x in txt:
        if x in '({':
            top += 1
            stack[top] = x
        elif x in ')}':
            if top == -1:   # 스택이 비면
                ans = 0
                break
            else:
                if (stack[top] == '(' and x == ')') or (stack[top] == '{' and x == '}'):
                    top -= 1
                else:
                    ans = 0
                    break

    if top > -1:
        ans = 0
    print(f"#{tc} {ans}")
