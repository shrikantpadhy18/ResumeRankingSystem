from django.db import models

# Create your models here.

class CompanyDetail(models.Model):
    state=models.CharField(max_length=15)
    city=models.CharField(max_length=15)
    zipcode=models.CharField(max_length=6)
    email=models.CharField(max_length=20)
    address1=models.CharField(max_length=40)
    address2=models.CharField(max_length=30)
    password=models.CharField(max_length=12)
    
    