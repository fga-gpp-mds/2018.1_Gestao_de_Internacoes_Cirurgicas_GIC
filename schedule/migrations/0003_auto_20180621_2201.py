# Generated by Django 2.0.3 on 2018-06-21 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0002_auto_20180517_2323'),
    ]

    operations = [
        migrations.AlterIndexTogether(
            name='occurrence',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='occurrence',
            name='event',
        ),
        migrations.DeleteModel(
            name='Occurrence',
        ),
    ]
