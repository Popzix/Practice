# Generated by Django 4.0.5 on 2022-06-29 10:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_alter_auction_item_category_alter_auction_item_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction_item',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.comments'),
        ),
        migrations.AlterField(
            model_name='auction_item',
            name='person_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.people'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='person_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='auctions.people'),
        ),
        migrations.AlterField(
            model_name='people',
            name='comments',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.comments'),
        ),
    ]