# z找出序列中出现次数最多的元素
# collections 模块中的counter 类正是为此类问题所涉及，most_common()方法可以直接告诉我们答案

words = [
    'look','into','wang','lei','yu','eyes','xia','shan','feng',
    'look','fei','wang','lei','lei','feng','yu','shan','kai',
    'wang','fei','yu','xiao','wang','feng','yu','shan','kai',
    'look','fei','wang','eyes','lei','hello','yu','yu','kai'
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)   # outputs  [('yu', 5), ('lei', 4), ('wang', 3)]

print(word_counts['red'])

# 如果想手动增加计数，只需简单的自增即可
morewords = ['why','are','you','not','looking','in','my','eyes']
for word in morewords:
    word_counts[word] += 1

print(word_counts['eyes'])

# 另一种方式使用update() 方法
word_counts.update(morewords)

a = Counter(words)
b = Counter(morewords)
print(a)
c = a + b
print(c)