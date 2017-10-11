my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}

def tups(l):
  a = l.items() #creates list
  b = tuple(a) #converts to tuple
  return a #returns new tuple
