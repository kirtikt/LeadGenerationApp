# Generated by Django 3.2.5 on 2023-01-13 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LeadGenerationApp', '0014_calldetail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calldetail',
            name='transactionid',
        ),
    ]
