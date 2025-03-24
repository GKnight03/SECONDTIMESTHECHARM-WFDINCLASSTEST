class Phone:
    def __init__(self, brand, model, release_year, cost, colour):
        self.brand = brand
        self.model = model
        self.release_year = release_year
        self.cost = cost
        self.colour = colour
    
    def display_info(self):
        print(f"Brand: {self.brand} | Model: {self.model} | Year: {self.release_year} | Price: {self.cost} | Colour: {self.colour}")
    
    def update_brand(self, brand):
        if isinstance(brand, str):
            self.brand = brand
    
    def update_model(self, model):
        if isinstance(model, str):
            self.model = model
    
    def update_year(self, release_year):
        if isinstance(release_year, int):
            self.release_year = release_year
    
    def update_price(self, cost):
        if isinstance(cost, (int, float)):
            self.cost = cost
    
    def update_colour(self, colour):
        if isinstance(colour, str):
            self.colour = colour

class Smartphone(Phone):
    def __init__(self, brand, model, release_year, cost, colour, operating_system, storage_capacity):
        super().__init__(brand, model, release_year, cost, colour)
        self.operating_system = operating_system
        self.storage_capacity = storage_capacity
    
    def display_info(self):
        super().display_info()
        print(f"Operating System: {self.operating_system} | Storage: {self.storage_capacity}GB")
    
    def update_os(self, operating_system):
        if isinstance(operating_system, str):
            self.operating_system = operating_system
    
    def update_storage(self, storage_capacity):
        if isinstance(storage_capacity, int):
            self.storage_capacity = storage_capacity

# Creating instances
standard_phone = Phone("Nokia", "3310", 2000, 50, "Red")
advanced_phone = Smartphone("Apple", "iPhone 13", 2021, 999, "Slate", "iOS", 128)

# Display details
print("Phone Details:")
standard_phone.display_info()
print("\nSmartphone Details:")
advanced_phone.display_info()

# Modifying attributes
print("\nUpdating Phone:")
standard_phone.update_price(60)
standard_phone.update_colour("Blue")
standard_phone.update_year(2024)
print("Updated Phone Info:")
standard_phone.display_info()

print("\nUpdating Smartphone:")
advanced_phone.update_os("Android")
advanced_phone.update_brand("Samsung")
advanced_phone.update_model("Galaxy")
advanced_phone.update_storage(256)
advanced_phone.update_colour("Orange")
print("Updated Smartphone Info:")
advanced_phone.display_info()
