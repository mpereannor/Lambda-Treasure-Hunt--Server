# Generated by Django 2.1.4 on 2019-01-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0009_auto_20190102_1952'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='coordinates',
            field=models.CharField(default='()', max_length=32),
        ),
    ]