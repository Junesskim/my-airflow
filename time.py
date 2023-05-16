# from datetime import datetime
# from datetime import timedelta
# from dateutil.relativedelta import relativedelta

# target_date = datetime(2011, 11, 11)

# Before13_now = datetime.now() - relativedelta(year=13)
# now_local = datetime.now()

# local_date = now_local.strftime('%Y-%m-%d')

# print(target_date)
# print(Before13_now)

# print(now_local)

# print(local_date)

from datetime import datetime
from dateutil.relativedelta import relativedelta

now = datetime.now()

before_one_year = now - relativedelta(years=13)
print("1년 전 :", before_one_year)