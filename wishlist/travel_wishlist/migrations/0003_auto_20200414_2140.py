# Generated by Django 3.0.4 on 2020-04-15 02:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel_wishlist', '0002_auto_20200409_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='date_visted',
            new_name='date_visited',
        ),
    ]
