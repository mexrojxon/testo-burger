# Generated by Django 4.0.2 on 2022-03-27 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commentmodel',
            name='phone',
        ),
        migrations.AlterField(
            model_name='authormodel',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='author-avatars/', verbose_name='avatar'),
        ),
    ]