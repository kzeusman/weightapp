# Generated by Django 3.2.7 on 2023-01-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weight', '0003_alter_weight_memo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='memo',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]