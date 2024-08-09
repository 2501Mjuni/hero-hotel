from django.db import models

class Hall(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    chairs = models.IntegerField()
    speakers = models.IntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.CharField(max_length=20)
    address = models.CharField(max_length=255)
    date = models.DateField()
    time_start = models.TimeField()
    time_end = models.TimeField()
    people = models.IntegerField()
    activity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.surname} - {self.date} - {self.hall.name}"
