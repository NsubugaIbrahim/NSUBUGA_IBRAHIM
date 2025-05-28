class Animal:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        print(f"This {self.name} makes a sound")
    
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    def make_sound(self):
       print(f"My dog called {self.name} of breed {self.breed} says 'Woof Woof'")

class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
    def make_sound(self):
        print(f"My {self.color} cat called {self.name} says 'meow'")

cat = Cat("Kitty", "White")
dog = Dog("Mark", "German Shepherd")

cat.make_sound()
dog.make_sound()