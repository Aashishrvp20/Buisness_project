from django.db import models
from users.models import User
from inventory.models import Product

class Supplier(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    photo=models.ImageField(upload_to="imageL/",blank=True)
    pan_no=models.TextField(default=00)
    date_created=models.DateField(auto_created=True,default=None,blank=True)
    opening_blnc=models.DecimalField(max_digits=5,decimal_places=2,default=0)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    paid = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    is_paid = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    invoice_file = models.FileField(upload_to='invoices/', blank=True, null=True)

    def __str__(self):
        return f"Purchase #{self.id} from {self.supplier.name if self.supplier else 'Unknown'}"

class PurchaseItem(models.Model):
    purchase = models.ForeignKey(Purchase, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=12, decimal_places=2) 

    def save(self, *args, **kwargs):
       # increase item for only new product
        if not self.pk:  
            product = self.product
            product.stock += self.quantity
            product.save()
        super().save(*args, **kwargs)

class PurchaseReturn(models.Model):
    purchase = models.ForeignKey(Purchase, on_delete=models.CASCADE, related_name='returns')
    date = models.DateTimeField(auto_now_add=True)
    refund_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)

    def __str__(self):
        return f"Return for Purchase #{self.purchase.id}"

class PurchaseReturnItem(models.Model):
    purchase_return = models.ForeignKey(PurchaseReturn, related_name='items', on_delete=models.CASCADE)
    purchase_item = models.ForeignKey(PurchaseItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def save(self, *args, **kwargs):
       
        product = self.purchase_item.product
        product.stock -= self.quantity  
        product.save()
        super().save(*args, **kwargs)
