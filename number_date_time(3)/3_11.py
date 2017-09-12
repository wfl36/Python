# 随机数选择
# 从一个序列中随机抽取一个元素
import random
values = [1,2,3,4,5,6]
print(random.choice(values))
print(random.sample(values,2))
random.shuffle(values)
print(values)