# 查找替换文本

# 我想对字符串中的文本做查找和替换
text = 'yeah, but no, but yeah, but no ,but yeah'
print(text.replace('yeah','yep'))

# 针对更为复杂的模式，可以使用re模块中的sub() 函数/方法
import re
text = 'Today is 9/08/2017.pycon stars 6/18/2017.'
print(re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\2',text))

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
print(datepat.sub(r'\3-\1-\2',text))

from calendar import month_abbr
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2),mon_name,m.group(3))

print(datepat.sub(change_date,text))

newtext,n = datepat.subn(r'\3-\1-\2',text)
print(newtext,n)

