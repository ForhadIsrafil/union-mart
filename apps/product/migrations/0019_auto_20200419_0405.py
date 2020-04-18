# Generated by Django 3.0.4 on 2020-04-18 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0018_auto_20200417_2343'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentPhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.PositiveSmallIntegerField(blank=True, help_text='Phone Number.', max_length=11, null=True)),
                ('service_name', models.CharField(choices=[('Bkash', 'Bkash'), ('Rocket', 'Rocket'), ('Nagad', 'Nagad')], default=('Bkash', 'Bkash'), max_length=20)),
                ('image', models.ImageField(upload_to='service_image')),
            ],
            options={
                'verbose_name': 'Payment Phone Number',
                'verbose_name_plural': 'Payment Phone Numbers',
            },
        ),
        migrations.AlterModelOptions(
            name='cart',
            options={'verbose_name': 'Cart', 'verbose_name_plural': 'Carts'},
        ),
    ]