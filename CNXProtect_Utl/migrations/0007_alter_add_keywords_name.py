# Generated by Django 3.2.4 on 2022-02-04 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CNXProtect_Utl', '0006_add_keywords'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_keywords',
            name='name',
            field=models.TextField(max_length=200, null=True),
        ),
    ]