#Testing datetime and string from time modules
import datetime 
import time

#both return objects that must be separated
now = datetime.datetime.now()
print now  #print object all the way down to milliseconds
print ' today"s year = ', now.year, 'today"s hour = ', now.hour
today = datetime.date.today()
print " today's weekday, month, day of month, and year == ", today.strftime('%A:%m:%d:%Y')
print ' 12 hour time or 24 hour time format with AM or PM', today.strftime('%I/%H/%p')
tomorrow = datetime.timedelta(days=1)
yesterday = datetime.timedelta(days=-1)
print 'today is ', today
print 'tomorrow is ',  tomorrow
xmas = datetime.date(2017,12,25)
diff = xmas - today
print xmas 
print 'Chrismas is {} days away from today!'.format(diff)
print time.localtime(time.time())
# Returns time.struct_time(tm_year=2017, tm_mon=11, tm_mday=6, tm_hour=22, tm_min=57, tm_sec=12, tm_wday=0 "MONDAY", tm_yday=310, tm_isdst=0)
print time.asctime()
#Returns easier to read version Mon Nov 06 22:58:43 2017
