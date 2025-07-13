from django.db import models

UNIT_CHOICES = [
    ('pcs', 'Pieces'),
    ('kg', 'Kilograms'),
    ('litre', 'Litres'),
    ('box', 'Box'),
]

Entry_CHOICES=[('in', 'Stock In'), ('out', 'Stock Out')]

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    unit = models.CharField(max_length=10, choices=UNIT_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    low_stock = models.PositiveIntegerField(default=5)

    def is_low_stock(self):
        return self.stock <= self.low_stock

    def __str__(self):
        return self.name

class StockEntry(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    entry_type = models.CharField(max_length=10, choices=Entry_CHOICES)
    note = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.entry_type == 'out' and self.quantity > self.product.stock:
            raise ValueError("Not enough stock to remove.")
        if self.entry_type == 'in':
            self.product.stock += self.quantity
        elif self.entry_type == 'out':
            self.product.stock -= self.quantity
        self.product.save()
        super().save(*args, **kwargs)
