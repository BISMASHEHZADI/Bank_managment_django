# Generated by Django 5.0.1 on 2024-08-07 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='acc_no',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='balance',
            field=models.FloatField(default=0.0),
        ),
    ]
