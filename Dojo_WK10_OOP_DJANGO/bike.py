class bike(object):
    def __init__(self, price, max_speed, miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def display_miles(self):
        print self.miles;
        return
    
    def display_info(self):
        print "Price equals : ",self.price, 'Max speed equals: ', self.max_speed, "Miles equals: ", self.miles
        return self
    
    def ride(self):
        self.miles += 10
        return self
    
    def reverse(self):
        self.miles -= 5
        if self.miles < 0:
            self.miles = 0
        print self.miles
        return self

bike1 = bike('100','15', '30')
bike2 = bike('200', '20', '10')
bike3 = bike('250', '40', '5')
bike1.ride().ride().ride().reverse().display_info()
bike2.ride().ride().reverse().reverse().display_info()
bike3.reverse().reverse().reverse().display_info()