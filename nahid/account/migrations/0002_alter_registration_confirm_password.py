# Generated by Django 3.2.7 on 2021-10-09 05:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='confirm_password',
            field=models.CharField(max_length=10),
        ),
    ]