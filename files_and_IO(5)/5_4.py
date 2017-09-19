# 读写字节数据
# 你想读写二进制数据，比如图片、声音文件 使用模式为 rb 或 wb 的open 函数读取或写入二进制数据

# 在读取二进制数据时，需要指明的是所有返回的数据都是字节字符串格式的，而不是文本字符串。类似的，在写入的时候，必须保证参数是以字节形式对外暴露数据的对象 (比如字节字符串，字节数组对象等)。

#在读取二进制数据的时候，字节字符串和文本字符串的语义差异可能会导致一个潜在的陷阱。特别需要注意的是，索引和迭代动作返回的是字节的值而不是字节字符串。

t = 'Hello World'
print(t[0])
for c in t:
    print(c)

b = b'Hello World'
print(b[0])

# 如果你想从二进制模式的文件中读取或写入文本数据，必须确保要进行解码和编码操作
with open('test.txt','rb') as f:
    data = f.read(28)
    text = data.decode('utf-8')
    print(text)

with open('somefile.bin','wb') as f:
    f.write(b'Hello World')

with open('somefile.bin','wb') as f:
    text = 'Hello wang'
    f.write(text.encode('utf-8'))

import array
nums = array.array('i',[1,2,3,4])
with open('data.bin','wb') as f:
    f.write(nums)

a = array.array('i',[0,0,0,0,0,0,0,0])
with open('data.bin','rb') as f:
    f.readinto(a)

print(a)

# 文件不存在才能写入
# 你想像一个文件中写入数据，但是前提必须是这个文件在文件系统上不存在。也就是不允许覆盖已存在的文件内容。
with open('somefile','wt') as f:
    f.write('Hello\n')

# 可以在 open() 函数中使用 x 模式来代替 w 模式的方法来解决这个问题
# with open('somefile','xt') as f:
#     f.write('World!')

# 在写文件时通常会遇到的一个问题,不小心覆盖一个已存在的文件。一个替代方案是先测试这个文件是否存在，像下面这样：
import os
if not os.path.exists('somefile'):
    with open('somefile','wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')


