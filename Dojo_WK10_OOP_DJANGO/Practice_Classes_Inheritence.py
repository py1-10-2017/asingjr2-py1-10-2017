#Practicing Class Inhertence Concept

class Journal:
    mood = "Happy"  # Can define class variable
    choices = 0 #used as count of total colors

    def __init__(self, date, name, age):
        self.date = date
        self.name = name
        self.age = age
        Journal.choices += 1

    @classmethod
    def new_mood(cls, mood):
        cls.mood = mood

    def age_reset(self,age):
        self.age = age

    def both(self): #Date and name with string
        return "Today is {} and i am {}!'".format(self.date, self.name)

    def name_upper(self):
        return (self.name).upper()

    def perm_name_upper(self): #changes attribute permanently
        self.name = self.name.upper()
        print(self.name)

class Hungry_Journal(Journal):#new class
    mood = 'Thrilled'

    def __init__(self, date, name, age, favorite_game):
        super().__init__(date, name, age)
        self.favorite_game = favorite_game
#must init all attributes and define only new

class Sleepy_Journal(Journal):
    def __init__(self, date, name, age, bed_size, related_items = None):
        super().__init__(date, name, age)
        self.bed_size = bed_size
        if related_items is None:
            self.related_items = []
            print('Need to include some relate items Sir')
        else:
            self.related_items = related_items

    def show_related_items(self): #really useful to cycle through grouped lists of other objects instead of returning "object..."
        for i in self.related_items:#using attribute name for list
            print('Includes: ', i.both())


j1 = Journal('9/7/86', "arthur", 3)
j2 = Journal('1/20/88', 'Pooh', 14)
#print(help(Hungry_Journal))
j3 = Hungry_Journal('2/12/80', 'Piglet', 12, 'Metroid')
print(j3.__dict__)
j4 = Sleepy_Journal('8/20/17', 'Robbin', 34, 'King')
j4.tea = "Camommile"
print(j4.__dict__) #can still add like with regular classes
#left out related items so message printed and empyt list was created

j5 = Sleepy_Journal('1/13/08', 'Rosario', 47, 'Twin', [j1,j2,j3]) #originally printed "boject information so I turned related items input to string
j5 = Sleepy_Journal('1/13/08', 'Rosario', 47, 'Twin', [j1,j2,j3])
print(j5.__dict__)

print('Trying new function that includes for loop')
print(j5.show_related_items())

#Useful Function
print('Useful Function')
print(isinstance(j1, Journal)) #need two arguements  (instance, class
print(isinstance(j5,Journal))
print(isinstance(j4,Hungry_Journal)) #printed false because j4 is not HJ instance
print('\n')
print(issubclass(Hungry_Journal, Journal))
print(issubclass(Hungry_Journal, Sleepy_Journal)) #HJ is not subclass of SJ