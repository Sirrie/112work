class Animal(object):
    def __init__(self, name):
        self.name = name
        print "Creating an Animal named", name

    def speak(self):
        print self.name + " says: '%s'" % self.getSpeakingSound()
        
    def getSpeakingSound(self):
        return "<generic animal sound>"

class Dog(Animal):
    # override Animal's __init__, but still call it
    def __init__(self, name):
        # Call superclass's __init__ method
        super(Dog, self).__init__(name)
        # now do dog-specific things
        print "Creating a dog named", self.name

    # override Animal's getSpeakingSound entirely (do not call it)
    def getSpeakingSound(self):
        return "woof!"

class Cat(Animal):
    # override Animal's __init__, but still call it
    def __init__(self, name):
        # Call superclass's __init__ method
        super(Cat, self).__init__(name)
        # now do cat-specific things
        print "Creating a cat named", self.name

    # override Animal's getSpeakingSound entirely (do not call it)
    def getSpeakingSound(self):
        return "meow!"

animal1 = Dog("fred")      # prints: Creating an Animal named fred
                           #         Creating a dog named fred
animal2 = Cat("wilma")     # prints: Creating an Animal named wilma
                           #         Creating a cat named wilma