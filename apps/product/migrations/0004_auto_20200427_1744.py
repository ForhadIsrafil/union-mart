# Generated by Django 3.0.4 on 2020-04-27 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_auto_20200426_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='position',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slider',
            name='product_id',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='trend',
            name='position',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]