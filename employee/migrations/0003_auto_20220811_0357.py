# Generated by Django 2.0 on 2022-08-10 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20220811_0357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemodel',
            name='emp_id',
            field=models.CharField(default='emp298', max_length=70),
        ),
    ]