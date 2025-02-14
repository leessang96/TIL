for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i1 != i2:
            for i3 in range(1, 4):
                if i1 != i3 and i2 != i3:
                    print(i1, i2, i3)
# 근데 3개정도면 그냥 손으로 만들어 놓고 쓰는게 좋을거에요ㅋㅋㅋ 6개만 만들면 되니까
# 그래도 이정도의 코드는 이해를 하셔야 해요!!
# 6!이면 6중 for문 되겠죠

# 1, 2, 3이 아니면?
arr = [2, 3, 7]
for i1 in range(3):
    for i2 in range(3):
        if i1 != i2:
            for i3 in range(3):
                if i1 != i3 and i2 != i3:
                    print(arr[i1], arr[i2], arr[i3])

# 효율 면에서 좋아보이진 않죠?
# 모든 경우를 찾는게 최적화 없어서 쉬워보이지만, 생각보다 쉽지 않아요