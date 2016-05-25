import re
from datetime import datetime, timezone, timedelta

#从形如'2015-6-1 08:10:30'的字符串和时区中转换出timestamp的值
def to_timestamp(dt_str, tz_str):
	rMatch = re.match(r'(UTC)([\+\-]\d{1,2})(:00)', tz_str)
	deltahours = rMatch.group(2)
	tz_val = timezone(timedelta(hours=int(deltahours)))
	dday = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
	return dday.replace(tzinfo=tz_val).timestamp()

t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1
t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2