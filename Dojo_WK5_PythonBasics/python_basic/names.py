#Dictionary Assginment with counter, dictionary, and list with dictionary
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def pr(list1):
  for i in list1:
    print i['first_name'] + " " + i['last_name']
  
#prints key with value 
pr(students)

users = {
'Students': [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
'Instructors': [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
}
print '\n'
def ball(classroom):
  
  for job in classroom:
    print job
    co = 1
    
    for thing in classroom[job]:
     
      f_n = thing['first_name'].upper()
      l_n = thing['last_name'].upper()
      length =len(l_n) + len(f_n)
      print ('{} {} {} {}').format(co, f_n, l_n, length)
      co +=1
 
ball(users)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 