# Generated by Django 3.2.4 on 2022-03-24 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CNXProtect_Utl', '0010_master_data1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dictionary1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keywords', models.TextField()),
            ],
        ),
    ]
