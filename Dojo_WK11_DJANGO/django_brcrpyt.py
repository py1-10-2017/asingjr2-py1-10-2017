#bcrypt practice
import bcrypt       #installed moddule using pip
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')


b = EMAIL_REGEX.match('*@1.love')
if b:
    print 'hey'
else:
    print 'not true'
first = bcrypt.hashpw('random'.encode(), bcrypt.gensalt())
# create variable
#call hashpw method
# to create encode password insert string followed by .encode comma .gensalt
#to decode simple put in originally provided string and encode entire first encrypted password
print first


print bcrypt.checkpw('random'.encode(), first.encode())
#Will return true if a match to orignal string





