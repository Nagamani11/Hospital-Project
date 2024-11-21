# Generated by Django 5.1.1 on 2024-10-21 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instituteapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_no', models.IntegerField()),
                ('course_name', models.CharField(max_length=100)),
                ('course_fee', models.IntegerField()),
                ('course_date', models.DateField()),
                ('course_time', models.TimeField()),
                ('duration', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=100)),
            ],
        ),
    ]