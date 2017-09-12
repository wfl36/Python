# 基本的日期和时间转换

from datetime import timedelta
a = timedelta(days=2,hours=6)
b = timedelta(hours=4.5)
c = a + b
print(c.days)
print(c.seconds)

# 如果你想表示指定的日期时间
from datetime import datetime

a = datetime(2017,9,12)
print(a + timedelta(days=10))
b = datetime(2017,6,18)
d = a - b
print(d)

now = datetime.today()
print(now)

# 计算最后一个周五
from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date
print(get_previous_byday('Friday'))

