# Generated by Django 4.2.5 on 2023-11-17 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PaymentSoliq', '0003_carduser_card_money'),
    ]

    operations = [
        migrations.AddField(
            model_name='carduser',
            name='mail_user',
            field=models.EmailField(default='mominovsharif12@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]