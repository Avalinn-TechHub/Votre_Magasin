# Generated by Django 4.1.3 on 2023-01-23 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Auto_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Cname', models.CharField(max_length=30)),
                ('Cusername', models.CharField(max_length=30)),
                ('Cphone', models.CharField(max_length=13)),
                ('Cplace', models.CharField(max_length=30)),
                ('Aname', models.CharField(max_length=30)),
                ('Ausername', models.CharField(max_length=30)),
                ('Avehicleno', models.CharField(max_length=30)),
                ('Aphone', models.CharField(max_length=13)),
                ('Date', models.DateField()),
                ('Status', models.CharField(max_length=10)),
            ],
        ),


        migrations.CreateModel(
            name='Customer_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Email', models.CharField(max_length=30)),
                ('Phonenum', models.CharField(max_length=13)),
                ('Address', models.CharField(max_length=50)),
                ('Username', models.CharField(max_length=30)),
                ('Password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(max_length=30)),
                ('Username', models.CharField(max_length=30)),
                ('items', models.CharField(max_length=30)),
                ('catgry', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=30)),
                ('total', models.CharField(max_length=30)),
                ('date', models.DateField(max_length=30)),
                ('Autoname', models.CharField(max_length=30)),
                ('Status', models.CharField(max_length=10)),
            ],
        ),
    ]
