# Generated by Django 4.2.4 on 2023-09-08 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_auction_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='description',
            field=models.TextField(blank=True, max_length=124),
        ),
    ]
