# Generated by Django 3.0.1 on 2020-01-09 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymodels2', '0002_auto_20200109_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pexpdt',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='pmfdt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
