# 筛选序列中的元素
# 序列中含有一些数据，我们需要根据需要提取的值或根据某些标准对序列做删减
# 筛选序列中的数据，最简单的方法是使用列表推导式

mylist = [1,4,-5,10,-7,2,3,-1]
print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

#  列表递推的缺点，当输入结果比较大的话，产生一个庞大的结果

pos = (n for n in mylist if n > 0)
for x in pos:
    print(x)

# 筛选结果没法简单的表示在列表推导式或生成器表达式中
values = ['1','2','-3','-','4','N/A','5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
ivals = list(filter(is_int,values))
print(ivals)

import math
print([math.sqrt(n) for n in mylist if n > 0])

# 关于数据筛选，有一种情况是用新值替换掉不满足标准的值
clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)
clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)