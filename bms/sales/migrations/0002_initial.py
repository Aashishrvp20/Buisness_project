# Generated by Django 5.2.3 on 2025-07-13 10:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contact', '0001_initial'),
        ('inventory', '0001_initial'),
        ('sales', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='sale',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='contact.customer'),
        ),
        migrations.AddField(
            model_name='saleitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.product'),
        ),
        migrations.AddField(
            model_name='saleitem',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sales.sale'),
        ),
        migrations.AddField(
            model_name='salereturn',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='returns', to='sales.sale'),
        ),
        migrations.AddField(
            model_name='salereturnitem',
            name='sale_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.saleitem'),
        ),
        migrations.AddField(
            model_name='salereturnitem',
            name='sale_return',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='sales.salereturn'),
        ),
    ]
