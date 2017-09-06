# 与字典相关的计算
# 在字典上对数据执行各式各样的操作（求最小值，最大值，排序）

prices = {
    'ACME':45.23,
    'AAPL':612.78,
    'IBM':205.55,
    'HPQ':37.20,
    'FB':10.75,
}
# zip 将字典的键和值反转过来
min_prices = min(zip(prices.values(),prices.keys()))
print(min_prices)
max_prices = max(zip(prices.values(),prices.keys()))
print(max_prices)

# 对数据排序只需要配合zip() 再配合sorted() 就可以了

prices_sorted = sorted(zip(prices.values(),prices.keys()))
print(prices_sorted)

# 注意 zip 创建了一个迭代器，他的内容只能被消费一次

prices_and_name = zip(prices.values(),prices.keys())
min(prices_and_name)  # ok
#max(prices_and_name) # valueError

print(min(prices))
print(min(prices.values()))
print(max(prices))
print(max(prices.values()))

print(min(prices,key=lambda k: prices[k]))
print(max(prices,key=lambda k: prices[k]))

# 得到最小值的话，还需要额外的一次查找
min_value = prices[min(prices,key=lambda k: prices[k])]
print(min_value)