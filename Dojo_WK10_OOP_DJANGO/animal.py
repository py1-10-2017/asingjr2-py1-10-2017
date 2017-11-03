#Creating animal parent class and sub-classes

class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -= 5
        return self

    def display_health(self):
        print self.health
        return self

class Dog(Animal):
    def __init__(self, name, health):
        super(Dog, self).__init__(name, health)
        self.health = 150

    def pet(self):
        self.health += 10
        return self

class Dragon(Animal):
    def __init__(self, name, health):
        super(Dragon,self).__init__(name, health)
        self.health = 170

# ladybug = Animal('ladybug', 40)
# print ladybug.name
# print ladybug.display_health()

# ladybug.walk().walk().walk().run().run().display_health()

golden = Dog('Thunder', 200)
print golden.name
print golden.health
golden.walk().walk().walk().run().run().pet().display_health()