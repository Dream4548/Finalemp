# Generated by Django 4.1.3 on 2023-10-02 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empapp', '0008_detail_detail_education'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='detail_education',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empapp.education'),
        ),
    ]