# Generated by Django 4.0.4 on 2022-05-16 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicDetails', '0016_rename_addmission_course_addmissiondetails_admission_course_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentdetails',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]