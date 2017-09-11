# 从字符串中去掉不需要的字符

s = ' hello world \n '
print(s.strip())

t = '------hello======='
print(t.lstrip('-'))
print(t.rstrip('='))
print(t.strip('-='))
print(t)

# 对字符串里面的空格进行某些操作，应该使用其他技巧

print(s.replace(' ',''))
import re
print(re.sub('\s+',' ',s))

# 常用的去除字符的操作同某些迭代操作符结合起来，比如从文件中读取文本行。
# filename = 'example.txt';
# with open(filename) as f:
#     lines = (line.strip() for line in f)
#     for line in lines:
#         pass

# 它是创建一个迭代器，在所有产出的文本上都会执行strip操作

s = 'python\fis\tawesome\r\n'
print(s)
# 清理空格，先建立一个小型的转换表，然后使用translate()

remap = {
    ord('\t') : ' ',
    ord('\f') : ' ',
    ord('\n') : None
}
a = s.translate(remap)
print(a)

# 可以利用这种重新映射的思想进一步构建出更加庞大的转换表
import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD',a)
print(b)
print(b.translate(cmb_chrs))
