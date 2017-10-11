#Coin toss
#flipping coin...dojo recommends round function but i am using randrange!


import random
def toss():
    print('Starting Program')
    heads = 0#Toss_result is 1
    tails = 0#Toss_result is 2
    i=1
    while i <11:
        toss_result = random.randrange(1,5001)
        toss_result
        if toss_result == 1:
          heads+=1
          print("Attempt #1: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far").format(heads, tails)
        elif toss_result == 2:
          tails+=1
          print("Attempt #1: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far").format(heads, tails)
        i+=1

toss()