import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int, input().split())

    # A < B < C, 이고 A, B, C > 0
    eat = 0
    while True:
        if A >= B:
            eat += 1
            A -= 1
        elif B >= C:
            eat += 1
            B -= 1

        if A == 0 or B == 0:
            eat = -1
            break

        if A < B < C:
            break

    print(f"#{tc} {eat}")
