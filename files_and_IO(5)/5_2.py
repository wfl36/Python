# 将 print() 函数的输入重定向一个文件夹

with open('E:/Github/Python/files_and_IO(5)/test.txt','wt') as f:
    print('Hello World',file=f)

# ==> 关于输出重定向到文件中就这些了。但是有一点要注意的就是文件必须是以文本模式打开。如果文件是二进制模式的话，打印就会出错。

# 使用其他分隔符或终止符打印, 想使用 print() 函数输出数据，但是想改变默认的分隔符或者行尾符
print('ACME',50,91.5)
print('ACME',50,91.5,sep=',')
print('ACME',50,91.5,sep=',',end='!!\n')

for i in range(5):
    print(i)

for i in range(5):
    print(i,end=' ')

# 使用非空格符来输出数据的时候，给print() 函数传递一个seq 参数是最简单的方案。使用str.join() 可以完成同样的事情
# print(','.join('ACME','50','91.5'))
print('###########')
row = ('ACME',50,91.5)
print(','.join(str(x) for x in row))

