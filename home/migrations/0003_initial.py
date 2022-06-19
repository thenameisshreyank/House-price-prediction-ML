# Generated by Django 4.0.3 on 2022-06-19 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_liked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaname', models.CharField(max_length=50)),
                ('bhk', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=15)),
                ('bathroom', models.CharField(max_length=10)),
                ('duplex', models.CharField(max_length=5)),
                ('parking', models.CharField(max_length=10)),
                ('balcony', models.CharField(max_length=10)),
                ('totalcost', models.CharField(max_length=25)),
            ],
        ),
    ]
