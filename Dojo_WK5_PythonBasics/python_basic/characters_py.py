#Find Charaters; finding characters in a string list

def finder(list1, list2):
  new_list = []
  for thing in list1:
    if list2 in thing:
      new_list.append(thing)
  print(new_list)
  #return new_list
  
a = ['hey', 'boy', 'food']
b = ['man']
c = ['giants']
d = 'food'  
e = 'o'

finder(a,d)
finder(a,e)

print a[1]

print ('i' in "time")