from django.db import models

# Create your models here.
class Company(models.Model):
    company_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=200)
    location=models.CharField(max_length=100)
    about=models.TextField()
    type=models.CharField(max_length=100, choices=(
                                            ('IT','IT'),
                                            ('Non-IT','Non-IT'),
                                            ('Edtech','Edtech')
                                            ))
    added_date=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)

    def __str__(self):
        return self.name
    

class Employee(models.Model):
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    address=models.TextField()
    phone=models.CharField(max_length=12)
    about=models.TextField()
    position=models.CharField(max_length=50,choices=(                         ('Manager','manager'),
                              ('Developer', 'developer'),
                              ('Hr','hr')))
    company=models.ForeignKey(Company, on_delete=models.CASCADE)
