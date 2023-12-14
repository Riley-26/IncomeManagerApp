# Generated by Django 4.1.6 on 2023-12-13 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IncomeApp', '0003_remove_person_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='amount',
            field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='expense',
            name='name',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='income',
            name='amount',
            field=models.IntegerField(max_length=5),
        ),
        migrations.AlterField(
            model_name='income',
            name='name',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
