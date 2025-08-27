class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"This is a {self.make} {self.model}.")

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)  # Inherit parent attributes
        self.num_doors = num_doors

    def display_info(self):
        # This is an example of polymorphism - we're overriding the parent method
        super().display_info()
        print(f"It has {self.num_doors} doors.")

my_car = Car(make="Tesla", model="Model 3", num_doors=4)
my_car.display_info() # This will call the Car's overridden method

# The Polymorshism challenge
class Animal:
    def make_sound(self):
        # This is the default behavior
        print("The animal makes a sound.")

class Dog(Animal):
    def make_sound(self):
        print("The dog barks! 🐕")

class Cat(Animal):
    def make_sound(self):
        print("The cat meows! 🐈")

animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.make_sound()
    