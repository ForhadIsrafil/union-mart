# Generated by Django 3.0.4 on 2020-04-20 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0026_auto_20200420_0149'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderpayment',
            options={'verbose_name': 'Order and Payment', 'verbose_name_plural': 'Order and Payments'},
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='invoice_no',
            field=models.PositiveIntegerField(default=1, unique=True),
        ),
    ]
