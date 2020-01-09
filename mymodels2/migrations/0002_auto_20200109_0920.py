# Generated by Django 3.0.1 on 2020-01-09 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mymodels2', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.IntegerField(primary_key=True, serialize=False)),
                ('pname', models.CharField(max_length=100)),
                ('pcost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pmfdt', models.DateTimeField(auto_now_add=True)),
                ('pexpdt', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Framework',
        ),
        migrations.DeleteModel(
            name='Language',
        ),
    ]
