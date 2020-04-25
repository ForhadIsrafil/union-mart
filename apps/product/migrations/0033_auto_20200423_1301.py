# Generated by Django 3.0.4 on 2020-04-23 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0032_orderpayment_is_delivered'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reward',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='reward_images')),
                ('reward_title', models.CharField(blank=True, max_length=50, null=True)),
                ('position', models.PositiveSmallIntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='orderpayment',
            name='is_delivered',
            field=models.BooleanField(default=False, help_text='Is products are delivered?'),
        ),
    ]
