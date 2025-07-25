# Generated by Django 5.2.3 on 2025-07-13 10:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quotations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_no', models.IntegerField(null=True, unique=True)),
                ('invoice_date', models.DateField(auto_now_add=True)),
                ('product_name', models.CharField(blank=True, max_length=100)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('quantity', models.IntegerField(default=0)),
                ('amount', models.DecimalField(decimal_places=2, editable=False, max_digits=10)),
                ('note_desc', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('reference', models.ImageField(upload_to='quote/')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.customer')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.product')),
            ],
        ),
    ]
