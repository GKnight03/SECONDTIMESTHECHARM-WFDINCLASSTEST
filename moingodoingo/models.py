from django.db import models

class Car(models.Model):
    car_id = models.AutoField(Primary_key=True)
    serial_number = models.CharField(max_length=100, unique=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    colour = models.CharField(max_length=30)
    year = models.IntegerField()
    for_sale = models.BooleanField()
