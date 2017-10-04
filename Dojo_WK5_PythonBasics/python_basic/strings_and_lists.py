#Strings and Lists
#Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
print(words.find('day'))
print(words.replace('day', 'month',1))

#Min and max
x = [2,54,-2,7,12,98]
print(max(x))
print(min(x))

#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print(x[0])
print(x[len(x)-1])
x2 = [x[0], x[len(x)-1]]
print(x2)

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
print(sorted(x))
print(x)
x.sort()
print(x)
print(len(x))
mo_be= x[((len(x)/2)):]
alf=x[0:((len(x)/2))]
print(mo_be)
print(alf)
newx = alf+mo_be 
print(newx)
