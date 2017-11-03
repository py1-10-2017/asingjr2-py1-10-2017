# #Create Basic Car Class with attributes and simple method

# class car(object):
#     def __init__(self, price, speed, fuel, mileage):
#         self.price = price
#         self.speed = speed
#         self.fuel = fuel
#         self.mileage = mileage
#         if price > 10000:
#             self.tax = 0.16
#         elif price < 10000: 
#             self.tax = 0.12
    
#     def display_all(self):
#         info = [self.price, self.speed, self.fuel, self.mileage, self.tax]
#         for attribute in info:
#             return attribute

# car1 = car( '400','100mph', '25mpg', '9000')
# print car1
# print car1.price
# print car1.speed
# print car1.fuel
# print car1.mileage
# print car1.tax
# car1.display_all()
# car2 = car(60000, '100mph', '27mpg', '10000')
# car1.display_all()
# car3 = car(70000, '100mph', '14mpg', '100000')
# car1.display_all()
# car4 = car(80000, '100mph', '40mpg', '6000')
# car1.display_all()
# car5 = car(3000, '105mph', '21mpg', '15000')
# car1.display_all()
# car6 = car(9000, '80mph', '20mpg', '1000')
# car1.display_all()

#Practice Inheritence

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

#Phase 2
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

#Phase 3 Override
# class BaseClass(object):
#     def __init__(self):
#         self.x = 10   #basic value

#     def running(self):
#         print 'running'

# class InClass(BaseClass):
#     def __init__(self):
#         super(InClass, self).__init__()
#         self.x = 50   #changed for checking

#     def running(self):  #Can overright method as long as name is called the same way with same name
#         print 'walking'

# i = BaseClass()
# print i.x
# i = InClass()
# print i.x
# print i.running()

#Phase 4 Abstract Class
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

