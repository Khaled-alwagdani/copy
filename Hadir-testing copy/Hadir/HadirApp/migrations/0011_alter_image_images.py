# Generated by Django 3.2.5 on 2022-12-24 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HadirApp', '0010_auto_20221223_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='images',
            field=models.FileField(max_length=300, null=True, upload_to='Images/'),
        ),
    ]
