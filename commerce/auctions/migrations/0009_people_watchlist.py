# Generated by Django 4.0.5 on 2022-06-30 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auction_item_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='watchlist',
            field=models.CharField(max_length=60, null=True),
        ),
    ]
