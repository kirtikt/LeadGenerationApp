# Generated by Django 3.2.5 on 2023-01-09 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LeadGenerationApp', '0012_auto_20221230_0734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Administrator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobileno', models.CharField(default='', max_length=45)),
                ('adminname', models.CharField(default='', max_length=45)),
                ('password', models.CharField(default='', max_length=45)),
            ],
        ),
    ]
