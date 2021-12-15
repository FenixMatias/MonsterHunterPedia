# Generated by Django 2.2.6 on 2019-11-01 21:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('monsterpedia', '0002_auto_20191029_2111'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='armor',
            options={'ordering': ['namearmor', 'monster']},
        ),
        migrations.AlterField(
            model_name='armor',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
    ]
