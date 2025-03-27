# Generated by Django 5.1.7 on 2025-03-25 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PestDiseaseAnalysis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='plant_images/')),
                ('detected_issue', models.CharField(blank=True, max_length=200, null=True)),
                ('analysis_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
