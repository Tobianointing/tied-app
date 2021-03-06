# Generated by Django 3.1.6 on 2021-02-23 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('teider', models.CharField(max_length=50)),
                ('email', models.CharField(default='adeyokunnuo@gmail.com', max_length=50)),
                ('doctor', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=50)),
                ('question', models.CharField(max_length=200)),
                ('session_type', models.CharField(max_length=50)),
                ('session_time', models.CharField(max_length=50)),
                ('t_type', models.CharField(default='query', max_length=50)),
                ('price', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
        ),
    ]
