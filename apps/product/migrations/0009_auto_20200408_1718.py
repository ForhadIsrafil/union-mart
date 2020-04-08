# Generated by Django 3.0.4 on 2020-04-08 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20200408_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='trend',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Men', 'Men'), ('Women', 'Women'), ('Construction', 'Construction'), ('Home Eecorations', 'Home Eecorations'), ('Electronics', 'Electronics'), ('Others', 'Others'), ('Kids World', 'Kids World')], default=('Men', 'Men'), max_length=20, verbose_name='Product Category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='sub_category',
            field=models.CharField(choices=[('Watch', 'Watch'), ('Belt', 'Belt'), ('Wallet', 'Wallet'), ('Shoe', 'Shoe'), ('Sunglass', 'Sunglass'), ('Ornaments', 'Ornaments'), ('Phrase', 'Phrase'), ('Safety Equipments', 'Safety Equipments'), ('Tools', 'Tools'), ('Machinery', 'Machinery'), ('Hardware', 'Hardware'), ('Sanitary', 'Sanitary'), ('Washing Device', 'Washing Device'), ('Water Purifiers', 'Water Purifiers'), ('Kitchen & Cleaning', 'Kitchen & Cleaning'), ('CC Camera', 'CC Camera'), ('Earphone', 'Earphone'), ('Scale', 'Scale'), ('Storage Device', 'Storage Device'), ('Network Device', 'Network Device'), ('Health Care', 'Health Care'), ('Stationery', 'Stationery'), ('Rain Coa', 'Rain Coat'), ('Kids Toys', 'Kids Toys'), ('Bag', 'Bag')], default=('Watch', 'Watch'), max_length=20, verbose_name='Product Sub-Category'),
        ),
    ]
