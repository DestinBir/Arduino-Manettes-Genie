# Generated by Django 4.2.3 on 2023-08-05 03:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arduino', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='code',
            field=models.CharField(default=0, max_length=10, unique=True),
            preserve_default=False,
        ),
    ]
