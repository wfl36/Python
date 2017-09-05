# 保存最后N 个元素

from collections import deque

def search(lines,pattern,history = 5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)
# example use on a file

if __name__ == '__main__':
    with open('somefile.text') as f:
        for line,prevlines in search(f,'Python',5):
            for pline in prevlines:
                print(pline,end='')
            print(line,end='')
            print('-'*20)

# 斐波那（Fibonacci）数列
def fab(max):
    n,a,b = 0,0,1
    while n < max:
        #print(b)
        a,b = b,a + b
        n = n + 1

# print 打印导致函数可复用性差，改进版本返回一个list

def fab(max):
    n,a,b = 0,0,1
    L = []
    while n < max:
        L.append(b)
        a,b = b,a + b
        n = n + 1
    return L

for n in fab(5):
    print(n)

# 使用 yield 的版本
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1

q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
print(q.pop())
print(q.popleft())
