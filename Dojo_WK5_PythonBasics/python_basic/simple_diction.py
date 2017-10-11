#Dictionary exercise to take dictionary as argument and print items in sentences

user_height= int(input('Please enter your height in inches the press enter'))
user_weight = int(input('Please enter your weight in numbers then press enter'))
user_color= str(raw_input('Please enter your favorite color then press enter'))


your_specs = {'height':user_height, 'weight':user_weight, 'color':user_color}

me = {'height':6.3, 'weight':270, 'color': 'red'}
print (user_color)

def your_info(l):
  print ('You are {}').format(l['height'])
  print ('You weight {}').format(l['weight'])
  print ('You like shirts that are {}').format(l['color'])

your_info(your_specs)