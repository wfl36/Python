# 展开嵌套的序列   将一个多层嵌套的序列展开成一个单层列表

from collections import Iterable

def flatten(items,ignore_types=(str,bytes)):
    for x in items:
        if isinstance(x,Iterable) and not isinstance(x,ignore_types):
            yield from flatten(x)
        else:
            yield x
items = [1,2,[3,4,[5,6],7],8]

for x in flatten(items):
    print(x)

# 顺序迭代合并后的的排序迭代对象
# 有一系列排序序列，想将它们合并后得到一个排序序列并在上面迭代遍历
import heapq
a = [1,4,7,10]
b = [2,5,6,11]
for c in heapq.merge(a,b):
    print(c)

# heapq.merge() 需要所有输入序列必须是排过序的。特别的，它并不会预先读取所有数据到堆栈中或者预先排序，也不会对输入做任何的排序检测。
# 它仅仅是检查所有序列的开始部分并返回最小的那个，这个过程一直会持续直到所有输入序列中的元素都被遍历完。

# 迭代器代替while无线循环
CHUNKSIZE = 8192
def readers(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        #process_data(data)

def reader2(s):
    for chunk in iter(lambda: s.rev(CHUNKSIZE),b''):
        pass

import sys
f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10),''):
    n = sys.stdout.write(chunk)

#  iter 函数一个鲜为人知的特性是它接受一个可选的 callable 对象和一个标记 (结尾) 值作为输入参数。
# 当以这种方式使用的时候，它会创建一个迭代器，这个迭代器会不断调用 callable 对象直到返回值和标记值相等为止。
# 这种特殊的方法对于一些特定的会被重复调用的函数很有效果，比如涉及到 I/O调用的函数。
# 举例来讲，如果你想从套接字或文件中以数据块的方式读取数据，通常你得要不断重复的执行 read() 或 recv() ，并在后面紧跟一个文件结尾测试来决定是否终止。
# 使用一个简单的 iter() 调用就可以将两者结合起来了。其中lambda 函数参数是为了创建一个无参的 callable 对象，并为 recv 或 read() 方法提供了 size 参数。


