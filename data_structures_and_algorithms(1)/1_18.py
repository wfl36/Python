# 将名称映射到序列的元素中

from collections import namedtuple
Subscriber = namedtuple('Subscriber',['addr','joined'])
sub = Subscriber('jonesy@example.com','2012-10-19')
print(sub)
print(sub.addr)
print(len(sub))
addr,joined = sub
print(joined)

# 命名元组的主要作用是将代码同它所控制的元素位置解耦

def compute_cost(records):
    total = 0.0
    for rec in records:
        total +=rec[1] * rec[2]
    return total

Stock = namedtuple('Stock',['name','shares','price'])
def compute_cost(records):
    total = 0.0
    for rec in records:
        s = Stock(*rec)
        total += s.shares * s.price
    return total