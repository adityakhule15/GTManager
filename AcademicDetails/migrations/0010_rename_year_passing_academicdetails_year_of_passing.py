# Generated by Django 3.2.6 on 2022-04-10 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicDetails', '0009_auto_20220402_0113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academicdetails',
            old_name='year_passing',
            new_name='year_of_passing',
        ),
    ]
