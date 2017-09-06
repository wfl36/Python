# 从序列中移除重复项且保持元素简顺序不变

# 如果系列中是可哈希（hashable）的， 可以通过集合和生成器轻松解决

def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

a = [1,5,2,1,9,1,5,10]
print(list(dedupe(a)))

# 只有当序列中的元素是可哈希的时候才能这么做。如果想在不可哈希的对象（比如列表）序列中去除重复项，对上述代码稍作修改：

def dedupe(items,key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
# 参数key 的作用是指定一个函数用来将序列中的元素转换为可哈希的类型，这么做的目的是为了检测重复项

a = [{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
print(list(dedupe(a,key=lambda d: (d['x'],d['y']))))
print(list(dedupe(a,key=lambda d: d['x'])))

b = [1,5,2,1,9,1,5,10]
print(set(b))

