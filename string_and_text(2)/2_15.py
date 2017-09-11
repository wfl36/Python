# 给字符串中的变量名做插值处理

s = '{name} has {n} messages.'
print(s.format(name='Guido',n=3))

name = 'lei'
n = '26'
print(s.format_map(vars()))

# vars() 有一个微妙的特性是它能作用于类实例上

class Info:
    def __init__(self,name,n):
        self.name = name
        self.n = n

a = Info('wang',18)
print(s.format_map(vars(a)))

# format() 和 format_map() 的缺点则是没法优雅地处理缺少某个值的情况
# print(s.format(name = 'feng')) error

# 解决方法单独定义一个带有 __missing__() 方法的字典类

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

del n
print(s.format_map(safesub(vars())))


