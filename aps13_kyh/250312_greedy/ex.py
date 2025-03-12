def kfc(x):
    # 재귀호출의 특징1. 항상 종료 조건과 함께 한다.
    if x == 5:
        return

    # 재귀 호출 전 들어가야 할 로직
    print(x)
    kfc(x + 1)  # 다음 재귀 호출 (매개변수를 변경하면서 전달)
    # 돌아오면서 해야할 로직
    print(x)


kfc(0)
print("끝")