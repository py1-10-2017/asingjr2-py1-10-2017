#Practicing Class Creation
#Creating Color class, then journal class with variable (local scope) and instance variable with local local scope lol
#Age_multiplied function doesn't work!!!!!!!

class Color:
    def __init__(self, person, thing, animal, cost):  # self must be first as it references it self for other attributes
        self.person = person  # should keep the same for consistency
        self.thing = thing
        self.animal = animal
        self.cost = cost

    def person_cost(self):  # defining method specific to this class.  Must call self as arguement
        return "Person and Cost equal {} and {} respectively.".format(self.person, self.cost)
        # Used .format method and {} to easily create printed information for method
        #Indent spaces same as original for defining functions

color1 = Color("Josh", "Sheets", "Fox", "90")  # DO NOT need to type self, only attributes
color2 = Color("Arthur", "Towel", "Deer", "50")

'''
Defining instances using above structure is better than typing repeatable code as below:
color1.person = 'Josh'
color1.thing = 'Sheets'
color1.animal = 'Fox'
color1.cost = '90'

color2.person = 'Arthur'
color2.thing = 'Towel'
color2.animal = 'Deer'
color2.cost = '50'
'''
print(color1)
print(color2)
print(color1.person)
print(color1.cost)
print(color1.person_cost())
print(Color.person_cost(color2)) #Runs the same way above does, but must use instance as arguement
print(color2.person_cost()) #Prints identical but different way to call
#print(help(Color))

#Creating new Class
print('NEW CLASS CREATION AND EXPERIMENTATION'
      'CALLED'
      'JOURNAL')#Wanted to extend line for typying practice :)


class Journal:
    mood = "Happy"  # Can define class variable
    multi = 5  # Will be used for function later
    choices = 0 #used as count of total colors

    def __init__(self, date, name, age):
        self.date = date
        self.name = name
        self.age = age
        Journal.choices += 1

    @classmethod
    def new_multi(cls, multi):
        cls.multi = multi

    @classmethod
    def new_color_from_str(cls, str_thing):
        date, name, age = str_thing.split("*")#randomly chosen split item choice for string given linked variable separeted by *
        return cls(date,name,age)#required attributes for creation along with cls name

    def age_reset(self,age):
        self.age = age

    def both(self): #Date and name with string
        return "Today is {} and i am {}!'".format(self.date, self.name)

    def name_upper(self):
        return (self.name).upper()

    def perm_name_upper(self): #changes attribute permanently
        self.name = self.name.upper()
        print(self.name)

    def age_multiplied(self):
        self.age = (self.age * self.multi)
        # Important note for class...if you use class.multiple it takes that information, however, if you use "self.multiple" it will take class unless an instance attribute has been defined (i.e. j1.multiple = __).  See line 68 below

print (Journal.mood)
print('trying new stuff with class varaibele')
print(Journal.choices)# shows zero for counter result
j1 = Journal('9/7/86', "arthur", 3)#create instance of journal entry
print(Journal.choices) #now shows 1 in counter
print('/n')
print(j1) #prints object
print('\n' * 2)
print(Journal.both(j1)) #prints date, name, and string bit for j1
print('\n' * 2)
print(j1.both()) #same as calling class and entering arguement
print('\n' * 2)

print(j1.name_upper())#this was temp represenation of j1 name attribute
print('\n' * 2)
print(j1.both()) #previous attribute did not change attribute permanently
print('\n' * 2)
print(j1.perm_name_upper())
print('\n' * 2)
print(j1.both())
print('/n')
print(j1.mood)  # mood will print when call ed through instance object
print(Journal.mood)
print(j1.__dict__)  # prints out all attribute for instance
print(Journal.__dict__)  # prints what inside of main class to include attributes, variables, and functions

'''
you can change Class attributes which will be inherited by instances, or change specific instances which will preceed class information.  Attribute search works backward starting from instance instance <= class
'''
print('\n' * 2)
print('MESSING AROUND WITH VARIABLES')
# Class mood = Happy
print(j1.mood)
print(Journal.mood)
Journal.mood = "Really really tired"
print(j1.mood)
print(Journal.mood)
print(j1.__dict__)
j1.mood = "Pissed"
print(j1.mood) #changed instance attribute of mood to "pissed"
print(Journal.mood)
print(j1.__dict__)  # only instance mood change.  Now shows in __dict__
print('\n'*10)









print('Trying Function with instance attributes')
print(j1.age)  # prints 3 for inputed age
print(j1.age_multiplied(),
      j1.age)  # should multiply j1.age by class attribute of 5 or (3 * 5) since no instance attribute of multi has been defined
j1.multi = 10  # now defining multi
print(j1.age_multiplied(),
      j1.age)  # takes existence j1.age which was already increased, and then passes thru function using instance defined attribute instead of class attribute
print(j1.__dict__)  # again new attribute shows in dict

j2 = Journal("1/21/88", 'Mike', 4)
print(j2.multi)
Journal.new_multi(11)
print(j2.multi)
print(j1.multi)#instance defined attribute trumps cls defined attribute
print(j1.__dict__)
j1.age_reset(90)
print(j1.__dict__)#change in attribute worked

print('USING CLASS METHOD AS NEW CONSTRUCTOR')
entry1 = ('10/5/51*Joey*87')
j3 = Journal.new_color_from_str(entry1)
print(j3)
print(j3.__dict__)


print(j1.__dict__)
j1.age_reset(100)
print(j1.age)
print(j1.age_multiplied())
print(Journal.multi)
print(j1.multi)
j1.multi = 5
print(j1.age_multiplied())#doesnt work...need to referesh!!!!
#hello

















































