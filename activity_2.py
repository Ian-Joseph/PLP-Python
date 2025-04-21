# Base class (optional for shared structure)
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Subclasses with their own implementation of move()
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road.")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying in the sky.")

class Boat(Vehicle):
    def move(self):
        print("🚢 Sailing on the water.")

class Bicycle(Vehicle):
    def move(self):
        print("🚴 Pedaling on the trail.")

# Create objects
vehicles = [Car(), Plane(), Boat(), Bicycle()]

# Polymorphic behavior in action
for v in vehicles:
    v.move()