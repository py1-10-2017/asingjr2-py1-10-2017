#Foo and Bar
def test3(thing):
  if isinstance(thing, int) and (thing >1):
    arr1 = [2,3,5,7,9]
    if thing in arr1:
      print('Foo')
    elif ((thing**.5)%2==0):
      print('Bar')
    elif thing%2==0 or thing%3==0 or thing%4==0 or thing%5==0 or thing%6==0 or thing%7==0 or thing%8==0 or thing%9==0:
      print ("FooBar")
    # elif thing <2:
    #   return "FooBar"
    else:
      print ('Foo')
  else:
    print "FooBar"
    

test3(100)
