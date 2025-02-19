T = int(input())
for tc in range(1, T+1):
    
    str1 = input()  # 찾을 문자열    xypv
    str2 = input()  # 전체 문자열    eoggxypvsy
    # def solve(str1, str2):
    #
    #     n = len(str1)
    #     m = len(str2)
    #
    #     for i in range(m-n+1):
    #         for j in range(n):
    #             if str2[i+j] != str1[j]:
    #                 break
    #         else:
    #             return 1
    #     return 0
    #
    # str1 = input()  # 찾을 문자열
    # str2 = input()  # 전체 문자열
    # result = solve(str1, str2)
    # print(f"#{tc} {result}")


    def solve(str1, str2):
        n = len(str1)
        m = len(str2)

        i = j = 0
        while i < m and j < n:
            if str2[i] != str1[j]:
                i = i - j + 1
                j = 0
            else:
                i += 1
                j += 1

        if j == n:
            return 1
        else:
            return 0

    answer = solve(str1, str2)
    print(f"#{tc} {answer}")
