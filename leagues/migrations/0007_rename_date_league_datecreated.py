# Generated by Django 4.0.5 on 2022-08-25 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0006_alter_league_date_alter_match_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='league',
            old_name='date',
            new_name='dateCreated',
        ),
    ]