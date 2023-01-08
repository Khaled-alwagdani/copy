# Generated by Django 3.2.5 on 2022-12-22 17:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HadirApp', '0003_user_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='img',
            field=models.ImageField(default='', upload_to='User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='reg_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date registered'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='user', max_length=20),
        ),
    ]