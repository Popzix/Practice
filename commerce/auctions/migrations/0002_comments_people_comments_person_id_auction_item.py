# Generated by Django 4.0.5 on 2022-06-28 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('comments_id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='People',
            fields=[
                ('person_id', models.IntegerField(primary_key=True, serialize=False)),
                ('bids', models.CharField(max_length=60)),
                ('name', models.CharField(max_length=60)),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.comments')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='person_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='auctions.people'),
        ),
        migrations.CreateModel(
            name='Auction_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('photo', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=20)),
                ('comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.comments')),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auctions.people')),
            ],
        ),
    ]
