class Phone:
    def __init__(self, brand, model, year, price, colour):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.colour = colour
    
    def show_details(self):
        print(f"Brand: {self.brand} | Model: {self.model} | Year: {self.year} | Price: {self.price} | Colour: {self.colour}")
    
    def modify_brand(self, brand):
        if isinstance(brand, str):
            self.brand = brand
    
    def modify_model(self, model):
        if isinstance(model, str):
            self.model = model
    
    def modify_year(self, year):
        if isinstance(year, int):
            self.year = year
    
    def modify_price(self, price):
        if isinstance(price, (int, float)):
            self.price = price
    
    def modify_colour(self, colour):
        if isinstance(colour, str):
            self.colour = colour

class Smartphone(Phone):
    def __init__(self, brand, model, year, price, colour, os, storage):
        super().__init__(brand, model, year, price, colour)
        self.os = os
        self.storage = storage
    
    def show_details(self):
        super().show_details()
        print(f"Operating System: {self.os} | Storage: {self.storage}GB")
    
    def modify_os(self, os):
        if isinstance(os, str):
            self.os = os
    
    def modify_storage(self, storage):
        if isinstance(storage, int):
            self.storage = storage

# Creating instances
basic_phone = Phone("Nokia", "3310", 2000, 50, "Blue")
smartphone = Smartphone("Apple", "iPhone 13", 2021, 999, "Black", "iOS", 128)

# Display information
print("Phone Details:")
basic_phone.show_details()
print("\nSmartphone Details:")
smartphone.show_details()

# Updating values
print("\nModifying Phone:")
basic_phone.modify_price(60)
basic_phone.modify_colour("Red")
print("Updated Phone Details:")
basic_phone.show_details()

print("\nModifying Smartphone:")
smartphone.modify_os("Android")
smartphone.modify_storage(256)
print("Updated Smartphone Details:")
smartphone.show_details()
