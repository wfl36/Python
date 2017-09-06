# 对不原生支持比较操作的对象排序
# 同一个类的实例之间做排序，但它并不原生支持比较操作

class User:
    def __init__(self,user_id):
        self.user_id = user_id
    def __repr__(self):
        return 'User ({})'.format(self.user_id)

users = [User(23),User(3),User(99)]
print(users)
print(sorted(users,key=lambda u: u.user_id))

# 除了可以用lambda 表达式外，另一种方式是使用 operator.attrgetter()

from operator import attrgetter
print(sorted(users,key=attrgetter('user_id')))
