# 方向迭代

a = [1,2,3,4]
for x in reversed(a):
    print(x)

# 自定义类上实现__reversed__ 方法实现方向迭代

class Countdown:
    def __init__(self,start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

for rr in reversed(Countdown(10)):
    print(rr)
    
for rr in Countdown(10):
    print(rr)
