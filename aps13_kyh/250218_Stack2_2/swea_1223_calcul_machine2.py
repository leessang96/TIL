# T = 10
# for tc in range(1, T+1):
#     n = int(input())
#     calcul = list(input())
#
#     top = -1
#     stack = [0] * (n + 1)
#
#     for x in calcul:
#         if x not in  '+-/*.':
#             top += 1
#             stack[top] = int(x)
#         else:
#             op1 = stack[top]
#             top -= 1
#             op2 = stack[top]
#             top -= 1
#             if x == '+':
#                 top += 1
#                 stack[top] = op1 + op2
#             elif x == '-':
#                 top += 1
#                 stack[top] = op1 - op2
#             elif x == '/':
#                 top += 1
#                 stack[top] = op1 // op2
#             elif x == '*':
#                 top += 1
#                 stack[top] = op1 * op2
#             elif x == '.':
#                 if top == -2:
#                     print(f'#{tc} {stack[0]}')
#
# # 이렇게 하면 앞에서 출력해서 사칙연산의 우선순위를 지키지 못함

icp = {'+' : 1, '*' : 2}        # 스택 밖에서의 우선순위
isp = {'+' : 1, '*' : 2}        # 스택 안에서의 우선순위

T = 10
for tc in range(1, T+1):
    n = int(input())
    calcul = input()    # 중위식
    postfix = ''        # 후위식
    
    stack = []          # 스택생성
    # infix -> postfix
    for x in calcul:
        if x not in '+*':   # 피연산자(숫자)인 경우, postfix에 전달
            postfix += x
        else:               # 연산자인 경우 빈칸이 없으므로 == 안해도 됨
            # 스택에 연산자가 있고, 마지막 연산자보다 우선순위가 높지 않으면
            # 조건에 만족할 때 까지 pop
            while stack and isp[stack[-1]] >= icp[x]:
                postfix += stack.pop()
            # 스택이 비어있거나 마지막 연산자보다 우선순위가 높으면 push
            stack.append(x) # 스택에 우선 순위가 높은 연산자 push

    # 중위식이 끝나면 스택에 남은 모든 연산자를 pop
    while stack:
        postfix += stack.pop()
    # print(postfix)

    # 후위식 연산
    for x in postfix:
        if x in '+*':       # 연산자인 경우
            op2 = stack.pop()     # 오른쪽 피연산자
            op1 = stack.pop()     # 왼쪽 피연산자
            if x == '+':
                result = op1 + op2
            elif x == '*':
                result = op1 * op2
            stack.append(result)
        else:               # 피연산자인 경우 스택에 push
            stack.append(int(x))

    print(f'#{tc} {stack[-1]}')
