# Generated by Django 3.2.4 on 2022-03-25 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CNXProtect_Utl', '0011_dictionary1'),
    ]

    operations = [
        migrations.CreateModel(
            name='File1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notesfile', models.FileField(upload_to='media')),
            ],
        ),
    ]
