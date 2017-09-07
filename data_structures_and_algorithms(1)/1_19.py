#  同时对数据做转换和换算
# 需要调用一个换算（reduction）函数 （例如 sum() min() max()） 首先对数据做转换或筛选

# 在函数中使用生成器表达式
nums = [1,2,3,4,5]
s = sum(x * x for x in nums)
print(s)

import os
files = os.listdir('E:\\Github\\Python\\data_structures_and_algorithms(1)')
if any(name.endswith('.py') for name in files):
    print('there be python!')
else:
    print('sorry,no python')

s = ('ACME',50,123.45)
print(','.join(str(x) for x in s))

portfolio = [
    {'name':'GOOG','shares':50},
    {'name':'YHOO','shares':75},
    {'name':'AOL','shares':20},
    {'name':'SCOX','shares':65},
]

min_shares = min(s['shares'] for s in portfolio)
print(min_shares)
min_shares = min(portfolio,key=lambda s: s['shares'])