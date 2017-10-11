#Making Dict from separate but even length lists

name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

new = dict(zip(name, favorite_animal))
print(new)

#Good was is to use isinstance to first test type
def dmaker(a,b):
  new_dict = {}
  if isinstance(a,list) and isinstance(b,list):
    if len(a) > len(b):
      new_dict = dict(zip(a, b))
      return new_dict
    elif len(b) > len(a):
      new_dict = dict(zip(b,a))
      return new_dict
  else: 
    return "Need two lists"

dmaker(name, favorite_animal)