import time
import datetime

current = time.ctime()

def timer():
    print 'Starting date and time is {}'.format(current)
    req = raw_input('How seconds long should countdown be? ')
    print "Starting countdown for {} seconds".format(req)
    i = int(req)
    while i > 0:
        print (i)
        i -= 1 
        time.sleep(1) 
    print "Ending date and time is {}".format(current)

timer()