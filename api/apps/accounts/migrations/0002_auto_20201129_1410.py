# Generated by Django 3.1.1 on 2020-11-29 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='money',
            field=models.IntegerField(default=0, verbose_name='all money'),
        ),
    ]
