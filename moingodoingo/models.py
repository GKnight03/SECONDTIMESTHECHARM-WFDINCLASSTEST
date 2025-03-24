from django.db import models

class Car(models.Model):
    car_id = models.AutoField(Primary_key=True)
    serial_number = models.CharField(max_length=100, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=30)
    year = models.IntegerField()
    for_sale = models.BooleanField()

class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=50)
    state_province = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    
class Salesperson(models.Model):
    salesperson_id = models.AutoField(primary_key=True)
    last_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    
class Invoice(models.Model):
    invoice_id = models.AutoField(primary_key=True)
    invoice_number = models.CharField(max_length=50, unique=True)
    date = models.DateField()
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    salesperson = models.ForeignKey(Salesperson, on_delete=models.CASCADE)
