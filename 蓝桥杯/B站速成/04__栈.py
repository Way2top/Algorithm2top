# 先进先出

# 直接用列表模拟栈

stk = []

# 入栈
stk.append(1)
stk.append(2)
stk.append(3)
stk.append(4)
print(stk)

# 获取栈顶元素，不移除
print(stk[-1])

# 出栈
val = stk.pop()
print(val)
print(stk)
