# Base class
class Smartphone:
    def __init__(self, brand, model, storage):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.__battery_level = 100  # private attribute for encapsulation

    def make_call(self, number):
        print(f"Calling {number} from {self.model}...")

    def charge(self):
        self.__battery_level = 100
        print(f"{self.model} is fully charged.")

    def get_battery_level(self):  # method to access private attribute
        return self.__battery_level

    def use_phone(self, minutes):
        drain = minutes * 0.5
        self.__battery_level = max(0, self.__battery_level - drain)
        print(f"Used phone for {minutes} mins. Battery at {self.__battery_level}%.")

# Subclass for iPhone
class iPhone(Smartphone):
    def use_face_id(self):
        print(f"{self.model} is using Face ID to unlock.")

# Subclass for Android
class AndroidPhone(Smartphone):
    def customize_ui(self):
        print(f"{self.model} is customizing the home screen with widgets.")

# Creating objects
iphone = iPhone("Apple", "iPhone 15", "128GB")
android = AndroidPhone("Samsung", "Galaxy S23", "256GB")

# Using methods
iphone.make_call("123-456-7890")
iphone.use_face_id()
iphone.use_phone(30)
print("Battery:", iphone.get_battery_level(), "%")

android.make_call("987-654-3210")
android.customize_ui()
android.use_phone(45)
print("Battery:", android.get_battery_level(), "%")