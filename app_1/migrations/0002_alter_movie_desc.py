# Generated by Django 4.2.1 on 2023-06-05 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='desc',
            field=models.CharField(max_length=200),
        ),
    ]
