# Generated by Django 4.1.3 on 2023-10-02 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0005_remove_detail_detail_educationlevel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Educationlevel',
            new_name='Education',
        ),
        migrations.RenameField(
            model_name='education',
            old_name='Educationlevel',
            new_name='Education',
        ),
    ]
