def pattern_count(p, t):
    n = len(t)
    m = len(p)
    cnt = 0
    i = j = 0
    while i < n:
        if t[i] != p[j]:  # 다르면
            i = i - j + 1  # i - j 비교를 시작했던 위치
            j = 0
        else:  # 같으면
            i += 1
            j += 1
        if j == m:      # 패턴을 찾은 경우
            cnt += 1
            i = i - j + 1
            j = 0
    return cnt
    

def bruteforce(p, t):
    n = len(t)  # 전체 텍스트의 길이
    m = len(p)  # 찾을 패턴의 길이

    i = j = 0
    while i < n and j < m:
        if t[i] != p[j]:  # 다르면
            i = i - j + 1  # i - j 비교를 시작했던 위치
            j = 0
        else:  # 같으면
            i += 1
            j += 1

    if j == m:
        return i - j  # 패턴의 시작 인덱스
    else:
        return -1     # 패턴이 없는 경우


t = "TTTTTATTAATA"  # 전체 텍스트
p = "TTA"           # 찾을 패턴

print(bruteforce(p, t))
print(pattern_count(p, t))