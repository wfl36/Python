# 对齐文本字符串
# 以某种对齐格式将文本格式化处理
text = "Hello World"
print(text.ljust(20))
print(text.rjust(20))
print(text.center(20))

# 接受一个可选的填充字符
print(text.rjust(20,'='))
print(text.center(20,'*'))

# fromat() 函数可以用来完成对齐任务。需要做的就是合理的利用'<' '>',或是'^' 字符以及一个期望的宽度值

print(format(text,'>20'))
print(format(text,'<20'))
print(format(text,'^20'))

print(format(text,'=>20s'))
print(format(text,'*^20s'))

# 当格式化多个值的时，这些格式化代码可以用在format()方法中。

print('{:>10s} {:>10s}'.format('Hello','World'))

# format() 它并不是特定于字符串的。她能作用于任何值
x = 1.2345
print(format(x,'>10'))
print(format(x,'^10.2f'))

