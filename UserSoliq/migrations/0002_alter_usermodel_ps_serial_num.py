# Generated by Django 4.2.5 on 2023-10-27 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSoliq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='PS_serial_num',
            field=models.IntegerField(unique=True),
        ),
    ]
