# 在字符串的开头或结尾处做文本匹配
# 我们需要在字符串的开头或结尾指定的文本模式做检查，例如检查文件的扩展名、url协议类型

filename = 'spam.txt'
print(filename.endswith('.txt'))
print(filename.startswith('file'))

import os
filenames = os.listdir('.')
print(filenames)

print(any(name.endswith('.py') for name in filenames))

print([name for name in filenames if name.endswith(('.c','.py'))])

from urllib.request import urlopen

def read_data(name):
    if name.endswith(('http:','https:','ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices = ['http:','ftp:']
url = 'http://www.python.org'
#url.startswith(choices)
print(url.startswith(tuple(choices)))

filename = 'wang.txt'
print(filename[-4:] == '.txt')

import re
url = 'http://www.python.org'

print(re.match('http:|https:ftp:',url))



