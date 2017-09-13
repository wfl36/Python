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
print(datetime.today().weekday())
print(weekdays.index('Friday'))

# 计算当前月份的日期范围
# 你的代码需要在当前月份中循环每一天，想找到一个计算这个日期范围的高效方法
# 下面是一个由当前月份开始日和下一个月开始日组成的元组对象
from datetime import datetime,date,timedelta
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _,days_in_month = calendar.monthrange(start_date.year,start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date,end_date)

start_date = date.today().replace(day=1)
days_in_month = calendar.monthrange(start_date.year,start_date.month)
print(date.today().replace(day=1))
print(days_in_month)

a_day = timedelta(days=1)
print(a_day)
first_day,last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day

def date_range(start,stop,step):
    while start < stop:
        yield start
        start += step

for d in date_range(datetime(2017,9,13),datetime(2017,9,16),timedelta(hours=6)):
    print(d)