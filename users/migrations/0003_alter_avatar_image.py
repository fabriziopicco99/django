# Generated by Django 5.0.6 on 2024-07-04 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_avatar_email_alter_avatar_last_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avatar',
            name='image',
            field=models.ImageField(default='avatars/default.jpg', upload_to='avatars/'),
        ),
    ]