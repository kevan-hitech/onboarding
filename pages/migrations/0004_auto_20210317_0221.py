# Generated by Django 3.1.7 on 2021-03-17 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210317_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='edit_date',
            field=models.DateTimeField(auto_now=True, verbose_name='date of last edit'),
        ),
    ]
