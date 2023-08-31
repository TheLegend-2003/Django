# Generated by Django 4.2.4 on 2023-08-31 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_desc', models.CharField(max_length=300)),
                ('item_price', models.IntegerField()),
            ],
        ),
    ]
