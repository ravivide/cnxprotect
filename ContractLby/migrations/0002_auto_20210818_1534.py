# Generated by Django 3.2.4 on 2021-08-18 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ContractLby', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Dictionary',
        ),
        migrations.DeleteModel(
            name='Files',
        ),
    ]
