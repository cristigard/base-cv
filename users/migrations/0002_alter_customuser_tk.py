# Generated by Django 3.2.10 on 2022-02-28 10:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='tk',
            field=models.CharField(default=uuid.UUID('b3fd7ad1-3636-4341-8bfd-8a08d117424d'), max_length=255, primary_key=True, serialize=False, unique=True),
        ),
    ]