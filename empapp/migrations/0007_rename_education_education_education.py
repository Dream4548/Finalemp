# Generated by Django 4.1.3 on 2023-10-02 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0006_rename_educationlevel_education_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='education',
            old_name='Education',
            new_name='education',
        ),
    ]
