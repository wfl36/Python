# 在两个字典中寻找相同点
# 在两个字典中，找出它们中间可能相同的地方（相同的键，相同的值）

a = {
    'x' : 1,
    'y' : 2,
    'z' : 3
}

b = {
    'w' : 10,
    'x' : 11,
    'y' : 2
}
# find keys in common
print(a.keys() & b.keys())

# find keys in a that are not in b
print(a.keys() - b.keys())

# find (key,value) pairs in common
print(a.items() & b.items())

# 创建一个新字典，其中户去掉一些键  make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z','w'}}
print(c)

