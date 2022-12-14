# Generated by Django 3.1.5 on 2022-12-02 19:31

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('facedetection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='reportModel',
            fields=[
                ('reportId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('typeReport', models.CharField(choices=[('D', 'Daily'), ('W', 'Weekly'), ('M', 'Monthly')], max_length=1)),
                ('detectionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='report', to='facedetection.detectionmodel')),
            ],
            options={
                'db_table': 'report',
            },
        ),
    ]
