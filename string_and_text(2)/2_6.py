# 以不区分大小的方式对文本做查找和替换
# 需要使用re 模块并对各种操作都加上re.IGNORECASE

import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python',text,flags=re.IGNORECASE))
print(re.sub('python','snake',text,flags=re.IGNORECASE))

# 上面例子，待替代的文本与匹配的文本大小写并不吻合。要修正这个问题，需要用到一个支撑函数

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

print(re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE))