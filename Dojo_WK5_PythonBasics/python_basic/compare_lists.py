#Compare Lists

def compare(list1, list2):
  if list1==list2:
    print ('They are the same')
  else:
    print ('They are different')
    
list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
compare(list_one, list_two)


list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
compare(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
compare(list_one, list_two)

list_one = ['celery','carrots','cream','bread']
list_two = ['celery','carrots','bread','cream']
compare(list_one, list_two)

