# Generated by Django 2.2.7 on 2019-11-29 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsterpedia', '0006_auto_20191102_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='imagemonster',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%D/'),
        ),
    ]
