# 迭代器切片
# 你想得到一个迭代器生成的切片对象，但是标准切片切片操作并不能做到

def count(n):
    while True:
        yield n
        n += 1

c = count(0)
# print(list(c))
import itertools
for x in itertools.islice(c,10,20):
    print(x)

items = ['a','b','c',1,4,10,15]
for x in itertools.islice(items,None,3):
    print(x)

# 排列组合迭代
items = ['a','b','c']
from itertools import permutations
for p in permutations(items):
    print(p)

# 指定长度的所有排列组合，可以传递一个可选的长度参数
for p in permutations(items,2):
    print(p)

# 使用itertools.combinations() 可得到输入集合元素的所有的组合
print('==============')
from itertools import combinations
for c in combinations(items,3):
    print(c)

for c in combinations(items,1):
    print(c)

# ==> 对于combinations 来说，元素的顺序已经不重要了 也就是数 ('a','b')  和 ('b','a') 其实是一样的
# print(dir(itertools))


