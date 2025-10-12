from collections import Counter

s1 = 'nihao'
s2 = 'haoni'
s3 = 'nioah'

# Counter 接受可迭代对象作为传参
c1 = Counter(s1)
c2 = Counter(s2)
c3 = Counter(s3)

# 得到的是 collections.Counter 类型的类
print(c1, ' ', type(c1))
print(c2, ' ', type(c2))
print(c3, ' ', type(c3))

# Counter({'n': 1, 'i': 1, 'h': 1, 'a': 1, 'o': 1}) <class 'collections.Counter'>
# Counter({'h': 1, 'a': 1, 'o': 1, 'n': 1, 'i': 1}) <class 'collections.Counter'>
# Counter({'n': 1, 'i': 1, 'o': 1, 'a': 1, 'h': 1}) <class 'collections.Counter'>

if c1 == c2 == c3:
    print('Equals')
# Equals

# 这下面的操作是合法的，说明对于不存在的键会默认返回 0，不会像 dict 那样报错
print(c1['w']) # output: 0