# Generated by Django 4.2.8 on 2024-02-21 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0002_alter_akhila_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Akhilaa',
            fields=[
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('comments', models.CharField(max_length=400)),
            ],
            options={
                'db_table': 'Akhilaa',
            },
        ),
    ]
