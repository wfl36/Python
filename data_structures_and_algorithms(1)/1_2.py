#从任意可迭代对象中分解元素

record = ('dave','dave@example','789-456-123','147-852-963')

name,email,*phone_numbers = record

# * 式的语法在迭代一个变长的元组序列时尤其有用。例如，假如有一个带标记的元组序列

records = [
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4)
]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)

for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

# 特定字符串处理操作相结合，拆分操作的时候

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname,*fields,homedir,sh = line.split(':')
#print(homedir,sh)

# 有时候可能是分解某些值然后丢弃他们。  比如 _ 或 ign (ignored)

info = ('wang',50,123.45,(6,18,2017))
name,*_,(*_,year) = info
#print(year)

# 编写执行这类拆分功能的函数时，可实现精巧的递归算法

items = [1,10,7,4,5,9]
def sum(items):
    head,*tail = items
    return head + sum(tail) if tail else head

#print(sum(items))




