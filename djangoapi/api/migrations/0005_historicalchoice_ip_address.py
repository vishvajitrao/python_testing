# Generated by Django 3.2.4 on 2021-06-11 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210611_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalchoice',
            name='ip_address',
            field=models.GenericIPAddressField(default='127.0.1.1', verbose_name='IP address'),
        ),
    ]