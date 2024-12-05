# Generated by Django 5.1.3 on 2024-12-05 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_booking', '0003_room_room_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_number',
        ),
        migrations.AddField(
            model_name='room',
            name='number_status',
            field=models.PositiveSmallIntegerField(blank=True, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='цена'),
        ),
    ]