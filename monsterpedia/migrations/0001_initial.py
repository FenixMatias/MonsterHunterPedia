# Generated by Django 2.2.6 on 2019-10-29 02:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namespecies', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('namemonster', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('elements', models.CharField(max_length=500)),
                ('state', models.CharField(max_length=500)),
                ('weak', models.CharField(max_length=100)),
                ('habitat', models.CharField(max_length=1000)),
                ('size', models.IntegerField(default=0)),
                ('relative', models.CharField(max_length=500)),
                ('imagemonster', models.ImageField(upload_to='photos')),
                ('species', models.ManyToManyField(to='monsterpedia.Species')),
            ],
            options={
                'ordering': ['namemonster', 'title'],
            },
        ),
        migrations.CreateModel(
            name='Armor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namearmor', models.CharField(max_length=200)),
                ('information', models.CharField(max_length=3000)),
                ('imagearmor', models.ImageField(upload_to='photos')),
                ('monster', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monsterpedia.Monster')),
            ],
        ),
    ]
