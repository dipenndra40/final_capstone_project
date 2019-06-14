# Generated by Django 2.2.2 on 2019-06-14 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_code', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('hourly_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('max_hour_per_day', models.IntegerField()),
            ],
        ),
    ]
