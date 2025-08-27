# This is a class for a simple coffee machine.
# A class is like a blueprint for creating objects.
class CoffeeMachine:
    # This is the constructor. It's used to create a new object.
    # It takes a 'brand' and 'capacity' to set up the coffee machine.
    def __init__(self, brand, capacity_ml):
        self.brand = brand
        self.capacity_ml = capacity_ml
        self.is_on = False
        print(f"A {self.brand} coffee machine with a {self.capacity_ml}ml capacity has been created.")

    # This method turns the machine on or off.
    def power_on(self):
        self.is_on = True
        print(f"The {self.brand} coffee machine is now ON. ☕")

    # This method 'makes' a cup of coffee.
    def make_coffee(self):
        if self.is_on:
            print("Grinding beans and brewing coffee... ☕")
        else:
            print("The machine is OFF. Please turn it on first.")

# This is a subclass that inherits from the main CoffeeMachine class.
# It represents a more advanced machine that can make lattes.
class LatteMachine(CoffeeMachine):
    def __init__(self, brand, capacity_ml, has_frother):
        # We call the parent class's constructor to initialize its attributes.
        super().__init__(brand, capacity_ml)
        # We add a new attribute specific to the LatteMachine.
        self.has_frother = has_frother
        print(f"This advanced machine also has a frother: {self.has_frother}.")

    # This method overrides the parent's make_coffee method.
    # This is an example of polymorphism, as 'make_coffee' now behaves differently.
    def make_coffee(self):
        if self.is_on:
            # We call the parent method's make_coffee to reuse its logic.
            super().make_coffee()
            print("Steaming milk and making a delicious latte! 🥛")
        else:
            print("The machine is OFF. Please turn it on first.")


# --- Example Usage ---

# Create an instance of the basic coffee machine.
print("--- Creating a basic coffee machine ---")
basic_machine = CoffeeMachine("Nespresso", 500)
basic_machine.power_on()
basic_machine.make_coffee()

print("\n--- Creating an advanced latte machine ---")
# Create an instance of the LatteMachine class.
latte_machine = LatteMachine("Breville", 1200, True)
latte_machine.power_on()
latte_machine.make_coffee()

