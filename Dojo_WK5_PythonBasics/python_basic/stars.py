#Function that prints stars
def starzz(thing):
  print('*'*thing)

def letter_starzz(thing):
  print ((thing[0]) * len(thing))

def starynight(array):
  for item in array:
    if isinstance(item,int):
      starzz(item)
    if isinstance(item, str):
      letter_starzz(item) 


  