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
    
class appliedDetail(models.Model):
    email=models.CharField(max_length=30)
    name=models.CharField(max_length=30)
    mobile=models.CharField(max_length=11)
    gender=models.CharField(max_length=8)
    resumepath=models.FileField(upload_to='media')
    title=models.CharField(max_length=50)

    def __str__(self):
        return(self.title)

    


class jobdesc(models.Model):
    programmingL=models.CharField(max_length=60)
    database=models.CharField(max_length=60)
    frameworks=models.CharField(max_length=60)
    Experience=models.CharField(max_length=60)
    name=models.CharField(max_length=40)
    role=models.CharField(max_length=40)
    batch=models.CharField(max_length=50)
    registrationstart=models.CharField(max_length=50)
    registrationend=models.CharField(max_length=50)
    cid=models.CharField(max_length=30,default="itsdefaultvalue")
