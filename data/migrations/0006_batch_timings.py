# Generated by Django 3.2.3 on 2021-07-01 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20210701_2333'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='timings',
            field=models.CharField(max_length=100, null=True),
        ),
    ]