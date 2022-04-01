# Generated by Django 4.0.2 on 2022-04-01 07:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_teammodel_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammodel',
            name='position',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='team', to='pages.teampositionmodel', verbose_name='position'),
        ),
    ]