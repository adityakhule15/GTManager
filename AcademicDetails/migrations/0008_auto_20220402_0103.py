# Generated by Django 3.2.6 on 2022-04-01 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicDetails', '0007_auto_20220402_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addmissiondetails',
            name='addmission_id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='feesdetails',
            name='payment_id',
            field=models.CharField(max_length=1000, primary_key=True, serialize=False),
        ),
    ]
