# Generated by Django 3.2.5 on 2022-12-01 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeadGenerationApp', '0004_auto_20221201_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='photograph',
            field=models.CharField(default='', max_length=100),
        ),
    ]
