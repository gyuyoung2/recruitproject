# Generated by Django 3.2.2 on 2021-05-10 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210510_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recruit',
            old_name='name2',
            new_name='age',
        ),
    ]
