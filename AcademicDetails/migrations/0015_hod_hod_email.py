# Generated by Django 4.0.4 on 2022-05-12 10:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicDetails', '0014_remove_hod_hod_email_hod_hod_mobilenumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='hod',
            name='hod_email',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]
