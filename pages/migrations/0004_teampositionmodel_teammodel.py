# Generated by Django 4.0.2 on 2022-04-01 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_locationmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamPositionModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='name')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
            },
        ),
        migrations.CreateModel(
            name='TeamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25, verbose_name='first_name')),
                ('last_name', models.CharField(max_length=25, verbose_name='last_name')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('photo', models.ImageField(upload_to='', verbose_name='photo')),
                ('instagram_link', models.CharField(blank=True, max_length=50, null=True, verbose_name='instagram')),
                ('twitter_link', models.CharField(blank=True, max_length=50, null=True, verbose_name='twitter')),
                ('facebook_link', models.CharField(blank=True, max_length=50, null=True, verbose_name='facebook')),
                ('position', models.ManyToManyField(related_name='TeamPosition', to='pages.TeamPositionModel', verbose_name='Position')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Team',
            },
        ),
    ]