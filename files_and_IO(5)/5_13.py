# 获取文件夹中的文件列表
# 获取文件系统中的某个目录的文件列表

import os
names = os.listdir('E:\\Github\\Python\\files_and_IO(5)')
# print(names)

import os.path
names = [name for name in os.listdir('E:\\Github\\Python\\files_and_IO(5)') if os.path.isfile(os.path.join('E:\\Github\\Python\\files_and_IO(5)',name))]
print(names)

pyfiles = [name for name in os.listdir('E:\\Github\\Python\\files_and_IO(5)') if name.endswith('.py')]
print(pyfiles)

# 对文件名的匹配，可以考虑使用glob  或 fnmatch 模块
import glob
pyfiles = glob.glob('E:\\Github\\Python\\files_and_IO(5)\\*.py')

from fnmatch import fnmatch
pyfiles = [name for name in os.listdir('E:\\Github\\Python\\files_and_IO(5)') if fnmatch(name,'*.py')]
print(pyfiles)

# 获取目录中的列表是很容易的，但是其返回结果只是目录中实体名列表而已。
# 如果你还想获取其他的元信息，比如文件大小，修改时间等等，你或许还需要使用到os.path 模块中的函数或着 os.stat() 函数来收集数据。

pyfiles = glob.glob('*.py')
name_sz_date = [(name,os.path.getsize(name),os.path.getmtime(name)) for name in pyfiles]
for name,size,mtime in name_sz_date:
    print(name,size,mtime)

filte_metadata = [(name,os.stat(name)) for name in pyfiles]
for name,meta in filte_metadata:
    print(name,meta.st_size,meta.st_mtime)

#  最后还有一点要注意的就是，有时候在处理文件名编码问题时候可能会出现一些问题。
#  通常来讲，函数 os.listdir() 返回的实体列表会根据系统默认的文件名编码来解码。