from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('staff', 'Staff'),
        ('customer',"Customer"),
        ('instructor','Instructor'),
        ("student","Student")
    )
class User(AbstractUser):
    email = models.EmailField(unique=True)
    phone = PhoneNumberField(unique=True, null=False, blank=False,region='NP')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='customer')
    #   this changes username to email when authenticating 
    USERNAME_FIELD = 'email'
    # this is added since model might need to be added to login during amdin logins
    REQUIRED_FIELDS = ['username'] 

    def __str__(self):
        return self.email

  