# Generated by Django 3.2.5 on 2022-12-25 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HadirApp', '0016_auto_20221225_0758'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='img_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
