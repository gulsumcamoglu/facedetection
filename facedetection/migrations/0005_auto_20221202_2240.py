# Generated by Django 3.1.5 on 2022-12-02 19:40

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('facedetection', '0004_auto_20221202_2239'),
    ]

    operations = [
        migrations.CreateModel(
            name='detectionModel',
            fields=[
                ('detectionId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', models.ImageField(upload_to='uploads')),
                ('name', models.CharField(max_length=30)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'detection',
            },
        ),
        migrations.DeleteModel(
            name='reportModel',
        ),
    ]