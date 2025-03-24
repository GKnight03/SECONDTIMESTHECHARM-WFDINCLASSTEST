import unittest
from PartA import Phone, Smartphone

class PhoneTest(unittest.TestCase):
    def setUp(self):
        self.basic_phone = Phone("Nokia", "3310", 2000, 50, "Red")
        self.smartphone = Smartphone("Apple", "iPhone 13", 2021, 999, "Slate", "iOS", 128)

    def test_class_membership(self):
        self.assertIsInstance(self.basic_phone, Phone)
        self.assertIsInstance(self.smartphone, Smartphone)
    
    def test_not_incorrect_class(self):
        self.assertNotIsInstance(self.basic_phone, Smartphone)
        self.assertNotIsInstance(self.smartphone, Phone, msg="Smartphone is a subclass of Phone")
    
    def test_object_identity(self):
        reference_phone = self.basic_phone
        self.assertIs(self.basic_phone, reference_phone)
        self.assertIsNot(self.basic_phone, self.smartphone)
    
    def test_updates(self):
        self.basic_phone.modify_price(60)
        self.assertEqual(self.basic_phone.price, 60)
        
        self.basic_phone.modify_colour("Blue")
        self.assertEqual(self.basic_phone.colour, "Blue")
        
        self.basic_phone.modify_year(2024)
        self.assertEqual(self.basic_phone.year, 2024)
        
        self.smartphone.modify_os("Android")
        self.assertEqual(self.smartphone.os, "Android")
        
        self.smartphone.modify_brand("Samsung")
        self.assertEqual(self.smartphone.brand, "Samsung")
        
        self.smartphone.modify_model("Galaxy")
        self.assertEqual(self.smartphone.model, "Galaxy")
        
        self.smartphone.modify_storage(256)
        self.assertEqual(self.smartphone.storage, 256)
        
        self.smartphone.modify_colour("Orange")
        self.assertEqual(self.smartphone.colour, "Orange")

if __name__ == "__main__":
    unittest.main()
