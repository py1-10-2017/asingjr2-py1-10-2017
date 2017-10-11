#Fun with Functions Dojo Assignment
def oddeven():
      for i in range(0,501):
    print i
    if i%2==0:
      print i, "Is Even"
    if i%2!=0:
      print i, "Is Odd"
  
oddeven()

#Multiply a number by 5
a = [2,4,10,16]

def multiply(arr,num):
  l = []
  for thing in arr:
    thing = thing * num
    print thing
    l.append(thing)
  print l
  
multiply(a,5)