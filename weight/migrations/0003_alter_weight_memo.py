# Generated by Django 3.2.7 on 2023-01-21 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0002_alter_weight_datecompletes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='memo',
            field=models.TextField(blank=True, max_length=200),
        ),
    ]