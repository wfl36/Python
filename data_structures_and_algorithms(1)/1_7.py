# 让字典保持有序

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['apam'] = 3
d['grok'] = 4

for key in d:
    print(key,d[key])

#json 格式
import json
print(json.dumps(d))

# OrderedDict 内部维护一个双向链表，它会根据元素加入的顺序来排列键的位置。第一个新加入的元素被放置在链表的末尾。

