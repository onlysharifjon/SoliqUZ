# Generated by Django 4.2.5 on 2023-11-03 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('PaymentSoliq', '0002_alter_payment_user2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='pay_user',
        ),
    ]
