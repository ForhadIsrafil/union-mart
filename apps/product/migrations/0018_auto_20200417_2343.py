# Generated by Django 3.0.4 on 2020-04-17 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0017_product_discount'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sociallink',
            options={'verbose_name': 'Social Link', 'verbose_name_plural': 'Social Links'},
        ),
        migrations.RenameField(
            model_name='sociallink',
            old_name='complain_suggesion',
            new_name='complain_suggestion',
        ),
        migrations.AlterField(
            model_name='product',
            name='delevery_charge',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
