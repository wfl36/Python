# 通过公共键对字典列表排序
# 我们有一些列表，想根据一个或多个字段的值来对列表进行排序
# 利用 operator 模块 itemgetter

rows = [
    {'fname':'Brian','lname':'Jones','uid':1003},
    {'fname':'David','lname':'Beazley','uid':1002},
    {'fname':'John','lname':'Cleese','uid':1004},
    {'fname':'Big','lname':'Jones','uid':1001},
]

from operator import itemgetter

rows_by_fname = sorted(rows,key=itemgetter('fname'))
print(rows_by_fname)

rows_by_uid = sorted(rows,key=itemgetter('uid'))
print(rows_by_uid)

# itemgetter() 函数可以接受多个键

rows_by_lfname = sorted(rows,key=itemgetter('lname','fname'))
print(rows_by_lfname)

# 有时候会用lambda 表达试来取代 itemgetter() 功能

rows_by_fname = sorted(rows,key=lambda r: r['fname'])
print(rows_by_fname)
rows_by_lfname = sorted(rows,key=lambda r: (r['lname'],r['fname']))
print(rows_by_lfname)

# 该技术同样适用于min() max()
min(rows,key=itemgetter('uid'))
max(rows,key=itemgetter('uid'))