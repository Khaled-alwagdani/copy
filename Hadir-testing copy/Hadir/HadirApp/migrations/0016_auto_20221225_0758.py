# Generated by Django 3.2.5 on 2022-12-25 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HadirApp', '0015_alter_image_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='id',
        ),
        migrations.AddField(
            model_name='image',
            name='img_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]
