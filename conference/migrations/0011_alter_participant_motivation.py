# Generated by Django 4.0.6 on 2022-08-11 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0010_conference_created_conference_updated'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='motivation',
            field=models.TextField(max_length=50, null=True),
        ),
    ]
