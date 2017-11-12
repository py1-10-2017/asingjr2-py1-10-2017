# #Create Basic Car Class with attributes and simple method
#*****************************************************************************************************************************************
class car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.16
        elif price < 10000: 
            self.tax = 0.12
    
    def display_all(self):
        info = [self.price, self.speed, self.fuel, self.mileage, self.tax]
        for attribute in info:
            return attribute

car1 = car( '400','100mph', '25mpg', '9000')
print car1
print car1.price
car1.display_all()
print car.__dict__


#*****************************************************************************************************************************************
                                                        #Practice Inheritence           
#*****************************************************************************************************************************************
# class thing(object):
#     def __init__(self):
#         print'hello'
#         print 'wassup'
#     def ham(self):
#         print 'ham'

# class inherting_class(thing):  #To inherit a quality you simply pass parent class in as arguement
#     def __init__(self):
#         pass

# test1 = thing()
# test1.ham()     #Ham function now works because of parent class method

# try1 = inherting_class()
# try1.ham()          #Prints ham because it inherited from parent

# #Phase 1
# class Character(object):  #Inheritence also works with variables
#     def __init__(self):
#         self.health = 100

# class Hunter(Character):
#     def __init__(self):
#         super(Hunter, self).__init__()

# link = Hunter()
# print link.health


#*****************************************************************************************************************************************
                                                            #Phase 2
#*****************************************************************************************************************************************
# class Character(object):  #Inheritence also works with variables
#     def __init__(self, name):  #Added attribute name
#         self.health = 100
#         self.name = name

#     def print_name(self): #Added method print_name
#         print self.name

# class Hunter(Character):
#     def __init__(self, name, forge_name):  #Added name and forge_name
#         super(Hunter, self).__init__(name)  #added variable name in as arguement.have to pass associated variable
#         self.forge = Forge(forge_name)  #added class into this one.....possible define from parent or sibling classes

# class Forge:
#     def __init__(self, forge_name):
#         self.name = forge_name

# link = Hunter('Dylan', 'Emma')
# print link.health
# link.print_name()  #defined in parent class
# link.health  #defined in sibling class
# print link.forge.name

#*****************************************************************************************************************************************
                                                        #Phase 3 Override
#*****************************************************************************************************************************************
# class BaseClass(object):
#     def __init__(self):
#         self.x = 10   #basic value

#     def running(self):
#         print 'running'

# class InClass(BaseClass):
#     def __init__(self):
#         # super(InClass, self).__init__()
#         self.x = 50   #changed for checking



# i = BaseClass()
# print i.x
# j = InClass()
# print i.x
# print j.running()

#*****************************************************************************************************************************************
                                                        #Phase 4 Abstract Class
#*****************************************************************************************************************************************
# from abc import ABCMeta, abstractmethod

# class BaseClass(object):            #Trying to instanciate generates TypeError: Can't instantiate abstract class BaseClass with abstract methods ham
#     __metaclass__= ABCMeta

#     @abstractmethod
#     def ham(self):
#         print 'ham'

# class InClass(BaseClass):           #Can instanciate from inherited class
#     def ham(self):
#         print 'ham'

# # test1 = BaseClass() Error is thrown since class is abstract
# test1 = InClass()
# test1.ham()  #Works perfectly

#Phase 4 Multiple Inheritence
# from abc import ABCMeta, abstractmethod

# class Player(object):
#     armor = 'grey'
#     def __init__(self, name):
#         self.name = name
#         self.health = 100

# class Enemy(object):
#     __metaclass__ = ABCMeta
#     day = 'Monday'

#     @abstractmethod
#     def AttackPlayer(self,player):
#         pass
    
# class EnvironmentAsset(object):
#     __metaclass__=ABCMeta

#     @abstractmethod
#     def __init__(self):
#         self.mobile = False

# class Trap(Enemy, EnvironmentAsset):
#     def __init__(self):
#         super(Trap, self).__init__()

#     def AttackPlayer(self,player):      #Must override abstract class method otherwise you cannot instanciate
#          player.health -=10
#          return player.health       #returns change to player object!!!

# x = Trap()
# warrior = Player('warrior')
# print warrior.name
# print warrior.health
# x.AttackPlayer(warrior)
# print warrior.health   #No reflects change made by attackplayer method
# print warrior.armor     #Can print inherited armor color
# print Player.armor      #can print parent class armor color
# print x.day     #can take abstract class variable with no worries


# print Enemy.__subclasses__()

#*****************************************************************************************************************************************
                                                            #Phase 5 Multiple Args
#*****************************************************************************************************************************************
# def hey():
#     print 'Hello handsome'

# def bye(): #triple quotations needed to show in help function that gives direction or explanation of function
#     '''
#     Function prints say goodbye
#     '''
#     print 'Say goodbye'

# def food(fruit, *veggie):
#     '''
#     creating multiple string arguemnet
#     '''
#     print "i like " + fruit + ' and also i like ' + ','.join(veggie)  #Make sure to added spaces at beginning and end of string.



# food('apple')
# food('apple', 'corn', 'greens')
