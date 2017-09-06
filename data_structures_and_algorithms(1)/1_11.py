# 对切片的命名

record = '46465464632814782239631051325123456789147852123563147'
cost = int(record[20:32]) * float(record[40:48])

print(cost)

SHARES = slice(20,32)
PRICE = slice(40,48)
cost = int(record[SHARES]) * float(record[PRICE])
print(cost)

items = [0,1,2,3,4,5,6]
a = slice(2,4)
print(items[2:4])
print(items[a])
items[a] = [10,11]
print(items)
del items[a]
print(items)