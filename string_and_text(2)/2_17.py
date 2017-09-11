# 在文本中处理HTML和XML实体
# 我们想将&entity 或 &#code 这样的HTML 或是 XML 实体替换为它们想对应的文本。

s = 'elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))
print(html.escape(s,quote=False))

# 文本分词 有一个字符串，想从左到右将它解析为标记流
text = 'foo = 23 + 42 * 10'

import re
NAME = r'(?P<NAME>[a-zA_Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME,NUM,PLUS,TIMES,EQ,WS]))
scanner = master_pat.scanner('foo = 42')
print(scanner.match())

