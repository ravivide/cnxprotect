# Generated by Django 3.2.4 on 2022-03-15 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CNXProtect_Utl', '0009_rename_notesfile_file_pdf_notesfile1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Master_Data1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notesfile_11', models.FileField(upload_to='Master_File1')),
            ],
        ),
    ]
