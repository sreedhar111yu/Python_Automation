'''Inheritance - Animal Kingdom: Create a base class Animal with a method speak().
 Derive two classes Dog and Cat from Animal and override the speak method to reflect their sounds.'''

class animal:
    def sound(self):
        pass

class dog(animal):
    def sound(self):
        print('bark')

class cat(animal):
    def sound(self):
        print('meow')
        
class wolf(animal):
    def sound(self):
        print('woof')

d=dog()
c=cat()
d.sound()
c.sound()
