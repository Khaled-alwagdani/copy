# Generated by Django 3.2.5 on 2023-01-04 17:55

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HadirApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='classImgs',
            field=models.FileField(max_length=300, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='student',
            name='precense',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('presence_date', models.DateField(default=datetime.date.today, primary_key=True, serialize=False)),
                ('clas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='HadirApp.class')),
                ('student', models.ManyToManyField(to='HadirApp.Student')),
            ],
        ),
    ]