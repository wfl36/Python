# 实现优先级队列
# 实现一个队列，能够给定的优先级来对元素排序，每次pop操作都会返回优先级最高的那个元素

import heapq

class PriorityQueue:

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self,item,priority):  # 插入
        heapq.heappush(self._queue,(-priority,self._index,item))
        self._index += 1

    def pop(self): # 移除
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'),1)
q.push(Item('bar'),5)
q.push(Item('spam'),4)
q.push(Item('grok'),1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

# 补充说明 第一次执行pop() 操作时返回的元素具有最高的优先级，拥有相同优先级的两个元素（foo 和 grok） 返回顺序同他们插入到队列的顺序相同



