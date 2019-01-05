from datetime import datetime,timezone,timedelta
todaysdate=datetime.now() #this is called naieve time as it does not conatins time zone this is the cureent system time
'''we have to show timezone as by the reference of that we can show the users of diiferent country user time in there
time zones'''
print(todaysdate)

time_in_timezone=datetime.now(timezone.utc)
'''this is called aware time as it is aware of time zone 
there is one more lib that deals with dattime arrow
'''
print(time_in_timezone)

'''time delta give the difference b/w two date'''
#todays_time=datetime.now(timezone.utc)
todays_time=datetime.now()
tommarow_time=todays_time+timedelta(1)
print(todays_time)
print(tommarow_time)
'''time formating '''
format_time=todays_time.strftime("%Y-%m-%d %H:%M:%S") #strfdate= string format date
print(format_time)

'''aprt from date time there is sperate date and time module to work with date time'''