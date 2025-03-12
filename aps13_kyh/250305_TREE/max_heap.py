# 최대힙 (99 개의 값 저장가능한)
def enq(n):
    global last # 마지막 정점
    last += 1
    heap[last] = n  # 마지막 정점에 n 저장

    c = last        # 부모의 키 값과 비교하기 위해 
    p = c // 2      # 부모 정점 번호 계산
    while p and heap[p] < heap[c]: # 부모가 있고, 부모 < 자식 (최대힙 조건에 위반)
        heap[p], heap[c] = heap[c], heap[p]
        c = p       # 현재 부모를 자식으로
        p = c // 2  # 부모의 부모


def deq():
    global last
    tmp = heap[1]           # 루트 백업
    heap[1] = heap[last]    # 삭제할 노드의 키를 루트에 복사
    last -= 1               # 마지막 노드 삭제
    p = 1                   # 루트에 옮긴 값을 자식과 비교
    c = p * 2               # 왼쪽 자식
    while c <= last:        # 자식이 하나라도 있으면
        if c + 1 <= last and heap[c] < heap[c + 1]:     # 오른쪽 자식도 있고, 오른쪽 자식이 더 클 경우
            c += 1  # 비교 대상을 오른쪽 자식으로 정함
        if heap[p] < heap[c]:   # 자식이 더 크면 최대힙 규칙에 어긋나므로
            heap[p], heap[c] = heap[c], heap[p]
            p = c   # 자식을 새로운 부모로
            c = p * 2   # 왼쪽 자식 번호를 계산
        else:
            break
    return tmp


heap = [0] * 7
last = 0

enq(2)
enq(5)
enq(7)
enq(3)
enq(4)
enq(6)

print(heap)
while last:
    print(deq())