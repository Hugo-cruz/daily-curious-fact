# Generated by Django 3.2.9 on 2021-12-01 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_curiosities_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curiosities',
            name='text',
            field=models.TextField(max_length=200),
        ),
    ]
