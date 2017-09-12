# 数字的四设五入

print(round(1.23,1))

# 当一个刚好在两个值的中间的时候，round返回离它最近的偶数
print(round(1.5)) # 2
print(round(2.5)) # 2

x = 1.23456
print(format(x,'0.3f'))

a = 2.1
b = 4.2
c = a + b
print(c)
print(round(c,2))

# 执行精确浮点数计算
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)

from decimal import localcontext
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)

nums = [1.23e+18,1,-1.23e+18]
print(sum(nums))  # 0.0
# 以上错误可以利用math.fsum() 所提供的更精确计算能力来解决
import math
print(math.fsum(nums))

# 数字格式化输入
x = 1234.56789
print(format(x,'0.2f'))
print(format(x,'>10.1f'))
print(format(x,'<10.2f'))
print(format(x,'^10.2f'))
print(format(x,','))
print(format(x,'0,.1f'))

# 二八十六进制整数
x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

print(format(x,'b'))
print(format(x,'o'))
print(format(x,'x'))

print(int('4d2',16))
print(int('10011010010',2))

# 复数
a = complex(2,4)
b = 3 - 5j
print(a)
print(b)

print(a.real,a.imag,a.conjugate())
print(a + b)

# 执行其他复数函数比如正弦、余弦或平方根，使用cmath模块
import cmath
print(cmath.sin(a))
print(cmath.cos(a))

a = float('inf')
print(a)

# fractions 模块可以被用来执行包含分数的数学运算
from fractions import Fraction
a = Fraction(5,4)
b = Fraction(7,16)
print(a + b)
c = a * b
print(c)
print(c.numerator)
print(c.denominator)
print(float(c))








