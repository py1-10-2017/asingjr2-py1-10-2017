#Scores and Grades Assignment; range and if statments
import random
#Place import statements of top of document
#Basic grading system
def letter():
  for i in range(10):
    score = random.randrange(60,101)
    score
    if 60 <score < 70:
      print('Score is: ' + str(score) + 'Grade - D')
    if 70 <score < 80:
      print('Score is: ' + str(score) + 'Grade - C')
    if 80 <score < 90:
      print('Score is: ' + str(score) + 'Grade - B')
    if 90 <score < 101:
      print('Score is: ' + str(score) + 'Grade - A')

letter()