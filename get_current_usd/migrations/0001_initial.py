# Generated by Django 5.0.1 on 2024-01-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd', models.IntegerField()),
                ('rub', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
