# Generated by Django 5.0.1 on 2024-01-27 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='paid_until',
            field=models.DateField(auto_now_add=True),
        ),
    ]
