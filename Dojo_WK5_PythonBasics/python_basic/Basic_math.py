#Assignment: Multiples, Sum, Average
'''
Multiples
Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
'''

'''Multiples

Part I - Write code that prints all the odd numbers from 1 to 1000. Use the for loop and don't use a list to do this exercise.

Part II - Create another program that prints all the multiples of 5 from 5 to 1,000,000.
'''
num = 0
while(num < 1001):
  if(num % 2 !=0):
    print(num)
  num+=1

num2 = 0
while(num2 < 1000001):
  if(num2 % 5==0): #if % num = 0 its a multiple
    print(num2)
  num2+=1

#sum
a = [1, 2, 5, 10, 255, 3]
print(sum(a))
def sumer(list):
  print(sum(list))
  return sum(list)

b = [5,6]
sumer(b)

print('\n')

#Average
a = [1, 2, 5, 10, 255, 3]
def avg(list1):
  print(sum(list1))
  print(sum(list1)/len(list1))
  return(sum(list1)/len(list1))
  
boy = [10,10,55]
avg(boy)