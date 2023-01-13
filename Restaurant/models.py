from django.db import models

class Booking(models.Model):
    name = models.CharField(max_length=255)
    guests = models.IntegerField()
    booking_date = models.DateField()

    def __str__(self): 
        return self.name + " - " + self.booking_date.strftime("%b-%d-%Y")

class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
      return self.title
