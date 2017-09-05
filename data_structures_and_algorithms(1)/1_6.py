# 在字典中将键映射到多个值上

# 问题 我们想要一个将键（key） 映射到多个值的字典（即所谓的一键多值字典）

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)

d = {} # A regular dictionary
d.setdefault('a',[]).append(1)
d.setdefault('a',[]).append(2)
d.setdefault('c',[]).append(4)

#print(d)

# 原则上构建一个一键多值的很容易。但对第一个值做初始化操作，变得很杂乱。代码如下：
d = {}
for key,value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)

# 使用 defaultdict 后代码清晰很多

d = defaultdict(list)
for key,value in pairs:
    d[key].append(value)
