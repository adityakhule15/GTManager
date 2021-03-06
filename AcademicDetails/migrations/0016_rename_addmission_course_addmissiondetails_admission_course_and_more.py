# Generated by Django 4.0.4 on 2022-05-16 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicDetails', '0015_hod_hod_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addmissiondetails',
            old_name='addmission_course',
            new_name='admission_course',
        ),
        migrations.RenameField(
            model_name='addmissiondetails',
            old_name='addmission_course_group',
            new_name='admission_course_group',
        ),
        migrations.RenameField(
            model_name='addmissiondetails',
            old_name='addmission_date',
            new_name='admission_date',
        ),
        migrations.RenameField(
            model_name='addmissiondetails',
            old_name='addmission_id',
            new_name='admission_id',
        ),
        migrations.RenameField(
            model_name='addmissiondetails',
            old_name='addmission_year',
            new_name='admission_year',
        ),
        migrations.AlterModelTable(
            name='addmissiondetails',
            table='admissionDetails',
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=1000)),
                ('title', models.CharField(max_length=1000)),
                ('description', models.CharField(max_length=100000)),
                ('student_username', models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.SET_DEFAULT, to='AcademicDetails.studentdetails')),
                ('teachers_userName', models.ForeignKey(default='unknown', on_delete=django.db.models.deletion.SET_DEFAULT, to='AcademicDetails.teachersdetails')),
            ],
            options={
                'db_table': 'complaint',
            },
        ),
    ]
