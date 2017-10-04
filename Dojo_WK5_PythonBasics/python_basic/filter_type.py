# Filter by Type
def tester(thing):
      if type(thing) == int:
    if thing >= 100:
      print("That's a big number!")
    elif thing<=100:
      print("That's a small number!")
  if type(thing) == str:
    if len(thing.replace(" ",'')) >= 50:
      print("Long sentence")
    elif len(thing.replace(" ",'')) <= 50:
      print("Short sentence")
  if thing is list:
    if len(thing) >= 10:
      print("Big List")
    elif len(thing) >= 10:
      print("Short List")
  
    
sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

tester(sI)
tester(mI)
tester(bI)
tester(eI)
tester(spI)
tester(sS)
tester(mS)
tester(bS)
tester(eS)
tester(aL)
tester(mL)
tester(lL)
tester(eL)
tester(spL)


