# 字符串的 I/O 操作
# 你想使用操作类文件对象的程序来操作文本或二进制字符串
import io
s = io.StringIO()
s.write('Hello World\n')
print('This is a test',file=s)

print(s.getvalue())

s = io.StringIO('Hello\nWorld\n')
print(s.read(4))
print(s.read())

# io.StringIO 只能用于文本。如果你要操作二进制数据，要使用 io.BytesIO 类来代替。
s = io.BytesIO()
s.write(b'binary data')
print(s.getvalue())

# 固定大小记录的文件迭代
# 使用 iter 和 functools.partial() 函数：
from functools import partial

RECODE_SIZE = 32

# with open('somefile.data','rb') as f:
#     records = iter(partial(f.read,RECODE_SIZE,b''))
#     for r in records:
#         pass

# 读取二进制文件到可变缓冲区
import os.path
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename,'rb') as f:
        f.readinto(buf)
    return buf

# 内存映射的二进制文件
# 你想内存映射一个二进制文件到一个可变字节数组中，目的可能是为了随机访问它的内容或者是原地做些修改。
import os
import mmap
def memory_map(filename,access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename,os.O_RDWR)
    return mmap.mmap(fd,size,access=access)

# 为了使用这个函数，你需要有一个已创建并且内容不为空的文件。下面是一个例子，教你怎样初始创建一个文件并将其内容扩充到指定大小：
size = 1000000
with open('data','wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

m = memory_map('data')
print(len(m))
print(m[0:10])
print(m[0])
m[0:11] = b'Hello World'
m.close()

with open('data','rb') as f:
    print(f.read(11))

# mmap() 返回的 mmap 对象同样也可以作为一个上下文管理器来使用， 这时候底层的文件会被自动关闭。
with memory_map('data') as m:
    print(len(m))
    print(m[0:10])


