# Generated by Django 4.1.6 on 2023-12-12 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IncomeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
