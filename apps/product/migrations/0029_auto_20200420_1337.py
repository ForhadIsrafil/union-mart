# Generated by Django 3.0.4 on 2020-04-20 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0028_auto_20200420_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderpayment',
            name='payment_number',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
