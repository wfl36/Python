# 编写多行模式的正则表达式
# 我们打算用正则表达式对一段文字做匹配，希望匹配能够跨越多行

# 匹配C语言风格的注释
import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
...           muliline comment */
...'''

print(comment.findall(text1))
print(comment.findall(text2))

# 解决这个问题，可以添加对换行符的支持
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

# (?:.|\n) 指定了一个非捕获组（即，这个组只做匹配但不捕获结果，也不会分配组号）

# re.compile() 函数可以接受一个有用的标记-------re.DOTALL. 使得正则表达式中的句点（.） 可以匹配所有的字符，也包括换行符.

comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)
print(comment.findall(text2))

