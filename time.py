from datetime import datetime
from datetime import timedelta
import pytz

now = datetime.utcnow()

now_local = datetime.now()

local_date = now_local.strftime('%Y-%m-%d')


print(now)

print(now_local)

print(local_date)