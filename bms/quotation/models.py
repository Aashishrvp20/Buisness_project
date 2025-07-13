from django.db import models
from inventory.models import Product
from sales.models import Customer

class Quotations(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    customer=models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    voucher_no=models.IntegerField(unique=True,null=True)
    invoice_date=models.DateField(auto_now_add=True)
    product_name=models.CharField(max_length=100,blank=True)
    rate=models.DecimalField(decimal_places=2,max_digits=8)
    discount=models.DecimalField(max_digits=5,decimal_places=2)
    quantity=models.IntegerField(default=0)
    amount=models.DecimalField(max_digits=10,decimal_places=2,editable=False)
    note_desc=models.TextField()
    approved = models.BooleanField(default=False)
    reference=models.ImageField(upload_to="quote/")

    def save(self,*args, **kwargs):
        self.amount=(self.quantity*self.rate)-self.discount
        return super().save(*args,**kwargs)

    def __str__(self):
        return f"Quotation {self.voucher_no} - {self.product_name}"
    

    