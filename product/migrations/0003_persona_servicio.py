# Generated by Django 5.0.6 on 2024-06-12 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_animal_persona'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='servicio',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]