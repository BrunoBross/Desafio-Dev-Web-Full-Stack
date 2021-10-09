# Generated by Django 3.2.7 on 2021-10-09 01:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numbers', models.CharField(max_length=10)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('duodigit', models.BooleanField(default=False)),
            ],
        ),
    ]