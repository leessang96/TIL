# 큐 생성
queue = [0] * 3
front = rear = -1

# 1, 2, 3 인큐
rear += 1           # enqueue 1
queue[rear] = 1

rear += 1           # enqueue 2
queue[rear] = 2

rear += 1           # enqueue 3
queue[rear] = 3

while front != rear:    # 큐에 원소가 남아있으면
    front += 1          # 검사하고 꺼내는 동작이 많이 나옴
    t = queue[front]
#     print(t)
# print(queue)

# front += 1
# print(queue[front])
#
# front += 1
# print(queue[front])
#
# front += 1
# print(queue[front])

q = []
q.append(1) # enqueue 1
print(q)
q.append(2)
print(q)
q.append(3)
print(q)
print(q.pop(0)) # dequeue
print(q)
print(q.pop(0))
print(q)
print(q.pop(0))
print(q)