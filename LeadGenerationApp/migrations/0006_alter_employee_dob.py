# Generated by Django 3.2.5 on 2022-12-02 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeadGenerationApp', '0005_alter_employee_photograph'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateField(),
        ),
    ]
