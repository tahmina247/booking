# Generated by Django 5.1.3 on 2024-12-05 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_booking', '0002_country_country_name_en_country_country_name_ru_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='room_status',
            field=models.CharField(blank=True, choices=[('available', 'available'), ('booked', 'booked')], max_length=32, null=True),
        ),
    ]
