# Generated by Django 4.1.7 on 2023-03-01 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0003_test_drive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test_drive',
            name='Email',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
