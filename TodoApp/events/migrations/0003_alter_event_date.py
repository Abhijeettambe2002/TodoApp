# Generated by Django 5.1.4 on 2024-12-28 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_alter_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
