# Generated by Django 4.1.6 on 2023-12-10 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IncomeApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
