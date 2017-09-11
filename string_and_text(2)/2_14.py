# 字符串连接及合并

parts = ['Is','Chicago','Not','Chicago?']
print(' '.join(parts))
print(','.join(parts))

a = 'wang feng'
b = 'xiao yu'
print(a + ' ' + b)
print('{} {}'.format(a,b))

s = ''
for p in parts:
    s +=' '+ p
print(s)
# 不推荐上面的写法，因为每个+=操作都会创建一个新的字符串对象

data = ['ACME',50,91.1]
print(','.join(str(d) for d in data))

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

def combine(source,maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(),32168):
    #f.write(part) 写文件
    pass