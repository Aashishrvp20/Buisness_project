from django.db import models
from django.core.validators import RegexValidator
class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True, validators=[RegexValidator(regex=r'^\+?\d{7,15}$', message="Enter a valid phone number.")])
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    photo=models.ImageField(upload_to='imagesL/',blank=True)
    pan_no=models.TextField(default=00)
    date_created=models.DateField(auto_now_add=True)
    opening_blnc=models.DecimalField(max_digits=10,decimal_places=2,default=0)

    def __str__(self):
        return self.name

