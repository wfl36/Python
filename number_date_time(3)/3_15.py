# 字符串转换为日期
# 你的应用程序接受字符串格式的输入，但是你想将它们转换为datetime对象一边在上面执行非字符串操作

from datetime import datetime
text = '2017-09-01'
y = datetime.strptime(text,'%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)

# datetime.strptime() 方法支持很多格式化代码  这些格式化站位符也可以放过来使用
nice_z = datetime.strftime(z,'%A %B %d, %Y')
print(nice_z)

# strptime() 的性能比你想象中的差很多   如果已经知道日期格式 如 YYYY-MM-DD 你可像下面这样实现一个解析函数
from datetime import datetime
def parse_ymd(s):
    year_s,mon_s,day_s = s.split('-')
    return datetime(int(year_s),int(mon_s),int(day_s))


