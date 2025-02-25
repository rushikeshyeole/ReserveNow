# Generated by Django 4.2 on 2023-05-22 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Contact_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500)),
                ('Email', models.EmailField(max_length=254)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Customer_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cus_name', models.CharField(max_length=150)),
                ('Cus_time', models.TimeField()),
                ('Cus_people', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Thali_items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Rice', models.CharField(max_length=50)),
                ('G_bhaji', models.CharField(max_length=50)),
                ('S_bhaji', models.CharField(max_length=50)),
                ('Sweet', models.CharField(max_length=50)),
            ],
        ),
    ]
