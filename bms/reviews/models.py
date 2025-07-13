from django.db import models

# Create your models here.
class MyReview(models.Model):
    name=models.CharField(max_length=200)
    msg=models.TextField()
    rating=models.DecimalField(max_digits=5,decimal_places=1)
    logo_photo=models.ImageField(upload_to="user_image/")
    brand_post=models.TextField()
    

    def __str__(self):
        return self.name
    