# Generated by Django 3.2.10 on 2022-02-28 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='end_date',
            field=models.DateField(null=True, verbose_name='End date(leave empty for current position)'),
        ),
    ]
