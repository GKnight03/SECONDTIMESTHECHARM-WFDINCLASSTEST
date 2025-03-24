import unittest
from PartA import Phone, Smartphone

class PhoneTest(unittest.TestCase):
    def setUp(self):
        self.phone1 = Phone("Nokia", "3310", 2000, 50, "Red")
        self.phone2 = Smartphone("Apple", "iPhone 13", 2021, 999, "Slate", "iOS", 128)

    # Check object class membership
    def test_class_membership(self):
        self.assertIsInstance(self.phone1, Phone)
        self.assertIsInstance(self.phone2, Smartphone)
    
    # Ensure object is not a member of an unrelated class
    def test_not_incorrect_class(self):
        self.assertNotIsInstance(self.phone1, Smartphone)
        self.assertNotIsInstance(self.phone2, Phone, msg="Smartphone is a subclass of Phone")
    
    # Validate object identity
    def test_object_identity(self):
        ref_phone = self.phone1
        self.assertIs(self.phone1, ref_phone)
        self.assertIsNot(self.phone1, self.phone2)
    
    # Confirm updates apply
    def test_updates(self):
        self.phone1.modify_price(60)
        self.assertEqual(self.phone1.price, 60)
        
        self.phone1.modify_colour("Blue")
        self.assertEqual(self.phone1.colour, "Blue")
        
        self.phone1.modify_year(2024)
        self.assertEqual(self.phone1.year, 2024)
        
        self.phone2.modify_os("Android")
        self.assertEqual(self.phone2.os, "Android")
        
        self.phone2.modify_brand("Samsung")
        self.assertEqual(self.phone2.brand, "Samsung")
        
        self.phone2.modify_model("Galaxy")
        self.assertEqual(self.phone2.model, "Galaxy")
        
        self.phone2.modify_storage(256)
        self.assertEqual(self.phone2.storage, 256)
        
        self.phone2.modify_colour("Orange")
        self.assertEqual(self.phone2.colour, "Orange")

if __name__ == "__main__":
    unittest.main()