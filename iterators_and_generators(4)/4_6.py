# 带有外部状态的生成器函数

from collections import deque

class linehistory:

    def __init__(self,lines,histlen = 3):
        self.lines = lines
        self.hitory = deque(maxlen=histlen)

    def __iter__(self):
        for lineno,line in enumerate(self.lines,1):
            self.hitory.append((lineno,line))
            yield line

    def clear(self):
        self.hitory.clear()

with open('somefile.txt') as f:
    lines = linehistory(f)
    for line in lines:
        if 'Python' in line:
            for lineno,hline in lines.hitory:
                print('{}:{}'.format(lineno,hline),end='')

f = open('somefile.txt')
lines = linehistory(f)
# print(next(lines))
print(lines)
it = iter(lines)
print(next(it))

