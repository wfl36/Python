# 根据字段将记录分组
# 有一系列的字典或对象实例，我们想根据某个特定的字段（比如日期）来分组迭代数据

# itertools.groupby()函数对数据进行分组时特别有用

rows = [
    {'address':'5412 N CLARK','date':'07/01/2012'},
    {'address':'5148 N CLARK','date':'07/04/2012'},
    {'address':'5800 N 58TH','date':'07/02/2012'},
    {'address':'2122 N CLARK','date':'07/03/2012'},
    {'address':'5645 N RAVENSWOOD','date':'07/02/2012'},
    {'address':'1060 N ADDISON','date':'07/02/2012'},
    {'address':'4801 N BROADWAY','date':'07/01/2012'},
    {'address':'1039 N GRANVILLE','date':'07/04/2012'},
]

# 根据日期以分组方式迭代数据

from operator import itemgetter
from itertools import groupby

# sort by the desired field first
rows.sort(key=itemgetter('date'))

# Iterate in groups
for date,items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print(' ',i)

# 如果只是简单地根据日期将数据分组到一起，放进一个大数据结构中以允许进行随机访问，利用defaultdict()构建一个一键多值字典
from collections import defaultdict
rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
    
for r in rows_by_date['07/01/2012']:
    print(r)
