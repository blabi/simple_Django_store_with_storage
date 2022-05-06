# Generated by Django 4.0.2 on 2022-05-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=64)),
                ('slug', models.CharField(max_length=64, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('price', models.FloatField()),
                ('vat', models.IntegerField(choices=[(1, 0.23), (2, 0.08), (3, 0.05), (4, 0)])),
                ('stock', models.IntegerField()),
                ('categories', models.ManyToManyField(to='store_app.Category')),
            ],
        ),
    ]