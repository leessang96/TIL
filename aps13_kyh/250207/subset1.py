a = [2, 3, 7]
bit = [0] * 3
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            # print(bit)
            s = 0               # 합도 가능
            for b in range(3):
                if bit[b]:      # 1이면
                    print(a[b], end = ' ')      # 부분집합에 포함된 원소
                    s += a[b]   # 합
            print(bit, s)
            # 근데, 합을 찾을땐 보통 공집합 빼고 찾음

# 활용도는 떨어지지만, 우리가 구현할 수 있어야 함




