class Product(object):
    def __init__(self, price, item_name, weight, brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = 'for sale'
    
    def sell(self):
        self.status = 'sold'
        print self.status
        return self
  
    def add_tax(self):
        tax = .08 * self.price
        print tax + self.price
        return self
    
    def return_item(self, reason):
        self.reason = reason
        if reason == 'defective':
            self.price = 0
        if reason == 'box opened':
            self.price = .08 * self.price
            self.status = 'for sale'
        print self.price
        print self.status
        return self
    
    def display_info(self):
        info = [    
        self.price, 
        self.item_name,
        self.weight,
        self.brand,
        self.status]
        print info
        return self

shirt = Product(100, 'shirt', 2,'Nike')
print shirt
print shirt.price
shirt.sell()
shirt.add_tax()
shirt.return_item('broken')
shirt.return_item('box opened')
shirt.return_item('defective')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    