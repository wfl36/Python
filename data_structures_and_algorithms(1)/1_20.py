# 将多个映射合并为单个映射
a = {'x':1,'z':3}
b = {'y':2,'z':4}

from collections import ChainMap
c = ChainMap(a,b)
print(c['x'])
print(c['y'])
print(c['z'])

print(len(c))

print(list(c.keys()))
print(list(c.values()))
# 如果有重复的键值，会采用第一个映射中对应的值

# 修改映射的操作是会作用在列出的第一个映射上
c['z'] = 10
print(a)
c['w'] = 40
del c['x']
print(a)

#del c['y']  会报错  KeyError: "Key not found in the first mapping: 'y'"
print(b)

values = ChainMap()
values['x'] = 1
values = values.new_child()
values['x'] = 2
values = values.new_child()
values['x'] = 3
print(values)
