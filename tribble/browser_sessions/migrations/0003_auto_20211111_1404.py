# Generated by Django 3.1.7 on 2021-11-11 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browser_sessions', '0002_auto_20211111_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='description',
            field=models.CharField(default='asdf', max_length=512),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='session',
            name='name',
            field=models.CharField(default='asdf', max_length=128),
            preserve_default=False,
        ),
    ]
