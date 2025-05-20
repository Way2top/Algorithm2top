from collections import deque

# deque是双端队列，但是这里不管他的双端性，只用右端进左端出，当做队列来用
# 初始化
q = deque()
# 从队列队尾（右端）添加元素
q.append(1)
q.append(2)
q.append(3)
q.append(4)

# 弹出左边的元素
print(q.popleft())
print(q)
print(type(q))
