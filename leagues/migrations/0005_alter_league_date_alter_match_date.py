# Generated by Django 4.0.5 on 2022-08-25 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0004_league_myflavor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='match',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
