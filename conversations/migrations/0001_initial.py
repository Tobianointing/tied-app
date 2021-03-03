# Generated by Django 3.1.6 on 2021-02-23 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VoiceCall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('teider', models.CharField(max_length=50)),
                ('doctor', models.CharField(max_length=50)),
                ('total_time_used', models.IntegerField()),
            ],
        ),
    ]
