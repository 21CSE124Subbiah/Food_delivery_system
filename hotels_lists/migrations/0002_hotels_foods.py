# Generated by Django 5.0.4 on 2024-07-26 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_menu', '0002_remove_food_hotel'),
        ('hotels_lists', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotels',
            name='foods',
            field=models.ManyToManyField(related_name='hotelss', to='food_menu.food'),
        ),
    ]
