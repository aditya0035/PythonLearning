"""
TO work with DateTime in python we need to import datetime module
There are two kind of date in python
1.A date which does not have timezone attached to them is called naive datetime
2.A date which has timezone attached to them is called aware datetime
"""
from datetime import datetime
from datetime import timezone
from datetime import timedelta

current_date=datetime.now() #if no timezone is specified then it will read used system date time without timezone
print(current_date)

time_zone_date=datetime.now(timezone.utc)
print(time_zone_date) #here it will show time based on reference with UTC

#always store time in timezone format UTC commonly
#time deta give the diffence b/w two times

today_date=datetime.now()
tommaorw_date=today_date+timedelta(days=1)
#here time delta will add one day to the current date
print(tommaorw_date)