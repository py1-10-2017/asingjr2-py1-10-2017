#Create Basic Car Class with attributes and simple method

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
print car1.speed
print car1.fuel
print car1.mileage
print car1.tax
car1.display_all()
car2 = car(60000, '100mph', '27mpg', '10000')
car1.display_all()
car3 = car(70000, '100mph', '14mpg', '100000')
car1.display_all()
car4 = car(80000, '100mph', '40mpg', '6000')
car1.display_all()
car5 = car(3000, '105mph', '21mpg', '15000')
car1.display_all()
car6 = car(9000, '80mph', '20mpg', '1000')
car1.display_all()