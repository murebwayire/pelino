# Generated by Django 4.0.6 on 2022-07-23 06:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='speaker',
            options={'verbose_name': 'speaker', 'verbose_name_plural': 'speakers'},
        ),
    ]
