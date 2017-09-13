# 迭代器

items = [1,2,3]
it = iter(items)
print(next(it))
print(next(it))

# 代理迭代
# 构建一个自定义容器对象，里面包含有列表、元组或其他可迭代对象。你想直接在你的这个新容器上执行迭代操作

class Node:
    def __init__(self,value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'None({!r})'.format(self._value)

    def add_child(self,node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    # outputs node(1) node(2)
    for ch in root:
        print(ch)

# ==> python 的迭代器协议需要__iter__() 方法返回一个实现 __next__() 方法的迭代器对象

# 使用生成器创建新的迭代模式
def frange(start,stop,increment):
    x = start
    while x < stop:
        yield x
        x += increment
for n in frange(0,4,0.5):
    print(n)

print(list(frange(0,1,0.125)))

# 一个函数中需要有一个 yield 语句即可将其转换为一个生成器。跟普通函数不同的是，生成器只能用于迭代操作

def countdown(n):
    print('Starting to count from',n)
    while n > 0:
        yield n
        n -= 1
    print('Done!')

c = countdown(3)
print(c)
print(next(c))
print(next(c))
print(next(c))
print(next(c))




