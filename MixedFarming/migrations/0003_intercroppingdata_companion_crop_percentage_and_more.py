# Generated by Django 5.1.7 on 2025-03-24 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MixedFarming', '0002_croppingpattern_intercroppingdata_patterns'),
    ]

    operations = [
        migrations.AddField(
            model_name='intercroppingdata',
            name='companion_crop_percentage',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='intercroppingdata',
            name='patterns',
            field=models.ManyToManyField(related_name='intercropping_pattern', to='MixedFarming.croppingpattern'),
        ),
    ]
