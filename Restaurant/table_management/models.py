from django.db import models

class Customer_Table(models.Model):
    Cus_name = models.CharField(max_length=150)
    Cus_time = models.TimeField()
    # Cus_date = models.DateField()
    Cus_people = models.IntegerField()

class Customer_Contact_Details(models.Model):
    Name = models.CharField(max_length=500)
    Email = models.EmailField()
    Message = models.TextField()

class Thali_items(models.Model):
    Rice = models.CharField(max_length = 50)
    G_bhaji = models.CharField(max_length = 50)
    S_bhaji = models.CharField(max_length = 50)
    Sweet = models.CharField(max_length = 50)
# Create your models here.
