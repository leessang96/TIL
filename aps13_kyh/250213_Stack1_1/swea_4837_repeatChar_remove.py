'''
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX
'''

T = int(input())
for tc in range(1, T+1):
    str1 = input()
    n = len(str1)

    i = 0
    j = 1                           # 연속된 문자 확인용 인덱스
    while i < n-1:                  # i가 문자열 길이보다 하나 작게 = j 가 1로 할당되어서
        if str1[i] == str1[j]:      # 연속된 문자가 같을때
            str1 = str1[:i] + str1[j+1:]    # 해당 인덱스에 있는 친구들 제거
            n = len(str1)                   # 길이도 다시 할당
            i = 0                           # 처음부터 다시
            j = 1
            if n <= j:                      # 길이가 1이면 오류 발생 하므로 break
                break
        else:                               # 연속된 문자가 같지 않을때
            i += 1                          # 다음 인덱스로 하나씩 추가
            j += 1

    print(f"#{tc} {n}")