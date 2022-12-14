# Generated by Django 2.0 on 2022-08-10 21:27

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0003_auto_20220811_0357'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Name')),
                ('value', models.CharField(default='00,000.00', max_length=16)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('cash_out', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='employee.EmployeeModel')),
            ],
        ),
    ]
