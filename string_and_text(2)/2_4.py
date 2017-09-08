# 文本模式的匹配和查找

# 匹配简单的文字 str.find() str.endswith() str.startswith()

text = 'yeah, but no, but yeah, but no, but yeah'
print(text == 'yeah')
print(text.startswith('yeah'))
print(text.find('no'))

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

if re.match(r'\d+/\d+/\d+',text1):
    print('yes')
else:
    print('no')

dateat = re.compile(r'\d+/\d+/\d+')
if dateat.match(text1):
    print('yes')
else:
    print('no')

text = 'today is 11/27/2012. pycon starts 3/13/2013.'
print(dateat.findall(text))

dateat_n = re.compile(r'(\d+)/(\d+)/(\d+)')
m = dateat_n.match('11/27/2012')
print(m)
print(m.group(0))
print(m.group(1))
print(m.groups())

for month,day,year in dateat_n.findall(text):
    print('{}-{}-{}'.format(year,month,day))


