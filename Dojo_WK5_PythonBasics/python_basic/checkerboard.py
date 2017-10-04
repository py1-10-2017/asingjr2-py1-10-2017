#Checkerboard
a = ' '
b = '*'
c = (a+b)
d = (b+a)
c4 = c*4
d4 = d*4
twin_level = [c4, d4]
def board1(kool):
  kool = twin_level*4
  for i in kool:
    print i

ma =  6
board1(ma)


'''Better Way
def checkerboard():
    for i in range(0, 8):
        if i%2 == 0:
            print "* " * 4
        else:
            print " *" * 4
'''
