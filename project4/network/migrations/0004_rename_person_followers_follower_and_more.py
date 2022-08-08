# Generated by Django 4.0.5 on 2022-07-22 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0003_people_desc_posts_timestamp_alter_people_user_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='followers',
            old_name='person',
            new_name='follower',
        ),
        migrations.RemoveField(
            model_name='followers',
            name='name',
        ),
        migrations.AddField(
            model_name='followers',
            name='followed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Follower', to='network.people'),
        ),
    ]
