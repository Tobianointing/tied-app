# Generated by Django 3.1.6 on 2021-02-23 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('teider', models.CharField(max_length=50)),
                ('email', models.CharField(default='adeyokunnuo@gmail.com', max_length=50)),
                ('doctor', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=50)),
                ('t_type', models.CharField(default='appointment', max_length=50)),
                ('appointment_time', models.DateTimeField(default='2021-02-05 06:51:08+00:00')),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
