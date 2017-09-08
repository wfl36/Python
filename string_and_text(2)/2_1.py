# 针对任意多个的分隔符拆分字符串

# 需要将字符串拆分为不同的字段，但是分隔符（以及分隔符之间的空格）在整个字符串中并不一致

line = 'asdf fjdk; afed, fjek,asdf,    foo'
import re
print(re.split(r'[;,\s]\s*',line))

fields = re.split(r'(;|,|\s)\s*',line)
print(fields)

values = fields[::2]
delimiters = fields[1::2] + ['']
print(delimiters)
print(values)

str = ''.join(v+d for v,d in zip (values,delimiters))
print(str)

# 如果不想在结果中看到分隔字符，扔想用括号来对正则表达式模拟进行分组，可以保用非捕获组，以（？：...）的形式指定

print(re.split(r'(?:,|;|\s)\s*',line))