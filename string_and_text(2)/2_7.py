# 定义实现最短匹配的正则表达式

import re

str_pat = re.compile(r'\"(.*)"')
text1 = 'Computer says "no."'
print(str_pat.findall(text1))

text2 = 'Computer says "no." Phone says "yes."'
# 贪心策略，找出最长匹配
print(str_pat.findall(text2))

# 解决这个问题在 * 操作符号加上 ？ 修饰符
str_pat = re.compile(r'\"(.*?)\"')
print(str_pat.findall(text2))

