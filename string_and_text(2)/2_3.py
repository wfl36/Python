# 利用shell 统配符做字符串匹配

from fnmatch import fnmatch,fnmatchcase

print(fnmatch('foo.txt','*.txt'))
names = ['dat1.csv','dat2.csv','config.ini','foo.py']

print(fnmatch('foo.txt','*.TXT'))
print(fnmatchcase('foo.txt','*.TXT'))

