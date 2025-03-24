class Phone:
    def __init__(self, brand, model, year, price, colour):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.colour = colour
    
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Price: {self.price}, Colour: {self.colour}")
    
    def update_brand(self, brand):
        if isinstance(brand, str):
            self.brand = brand
    
    def update_model(self, model):
        if isinstance(model, str):
            self.model = model
    
    def update_year(self, year):
        if isinstance(year, int):
            self.year = year
    
    def update_price(self, price):
        if isinstance(price, (int, float)):
            self.price = price
    
    def update_colour(self, colour):
        if isinstance(colour, str):
            self.colour = colour

class Smartphone(Phone):
    def __init__(self, brand, model, year, price, colour, os, storage):
        super().__init__(brand, model, year, price, colour)
        self.os = os
        self.storage = storage
    
    def display_info(self):
        super().display_info()
        print(f"OS: {self.os}, Storage: {self.storage}GB")
    
    def update_os(self, os):
        if isinstance(os, str):
            self.os = os
    
    def update_storage(self, storage):
        if isinstance(storage, int):
            self.storage = storage

# Creating instances
basic_phone = Phone("Nokia", "3310", 2000, 50, "Blue")
smartphone = Smartphone("Apple", "iPhone 13", 2021, 999, "Black", "iOS", 128)

# Display information
print("Basic Phone Information:")
basic_phone.display_info()
print("\nSmartphone Information:")
smartphone.display_info()

# Performing updates
print("\nUpdating Basic Phone:")
basic_phone.update_price(60)
basic_phone.update_colour("Red")
print("Updated Basic Phone Information:")
basic_phone.display_info()

print("\nUpdating Smartphone:")
smartphone.update_os("Android")
smartphone.update_storage(256)
print("Updated Smartphone Information:")
smartphone.display_info()
 