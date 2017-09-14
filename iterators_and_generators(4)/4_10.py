# 系列索引值迭代
# 迭代一个序列的同时跟踪正在被处理的元素索引

my_list = ['a','b','c']
for idx,val in enumerate(my_list):
    print(idx,val)

# 按照传统行号（行号从1开始）,可以传递一个开始的行号
for idx,val in enumerate(my_list,1):
    print(idx,val)

def parse_data(filename):
    with open(filename,'rt') as f:
        for lineno,line in enumerate(f,1):
            fields = line.split()
            try:
                count = int(fields[1])

            except ValueError as e:
                print('Line {}: Parse error: {}'.format(lineno,e))

# enumerate() 对于跟踪某些值在列表中出现的位置是很有用的。
# 所以，如果你想将一个文件中出现的单词映射到它出现的行号上去，可以很容易的利用 enumerate() 来完成：
from collections import defaultdict
word_summary = defaultdict(list)
# with open('myfile.txt', 'r') as f:
#     lines = f.readlines()
#     for idx, line in enumerate(lines):
#         # Create a list of words in current line
#         words = [w.strip().lower() for w in line.split()]
#         for word in words:
#             word_summary[word].append(idx)

# 同时迭代多个序列
xpts = [1,5,4,2,10,7]
ypts = [101,78,37,15,62,99]
for x,y in zip(xpts,ypts):
    print(x,y)

#zip(a, b) 会生成一个可返回元组 (x, y) 的迭代器，其中 x 来自 a， y 来自 b。一旦其中某个序列到底结尾，迭代宣告结束。因此迭代长度跟参数中最短序列长度一致。
a = [1,2,3,]
b = ['w','x','y','z']
for i in zip(a,b):
    print(i)

# 如果这个不是你想要的效果，那么还可以使用 itertools.zip longest() 函数来代替。比如：
from itertools import zip_longest
for i in zip_longest(a,b):
    print(i)

for i in zip_longest(a,b,fillvalue=0):
    print(i)
