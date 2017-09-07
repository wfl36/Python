# 从字典中提取子集
# 创建一个字典，其本身是另一个字典的子集
# 利用字典推导式可以轻松解决

prices = {
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75,
}

# make a dictionary of all prices over 200
p1 = { key:value for key, value in prices.items() if value > 200 }
print(p1)

# make a dictionary of tech stocks
tech_names = { 'AAPL','IBM','HPQ','MSFT' }
p2 = { key:value for key,value in prices.items() if key in tech_names}
print(p2)
# 上面的例子还可以重写成：
p3 = { key:prices[key] for key in prices.keys() & tech_names}
print(p3)

