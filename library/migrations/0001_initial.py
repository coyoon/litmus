# Generated by Django 2.1.3 on 2018-11-17 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('hexa', models.CharField(max_length=6)),
                ('rgb_r', models.IntegerField()),
                ('rgb_g', models.IntegerField()),
                ('rgb_b', models.IntegerField()),
            ],
        ),
    ]
