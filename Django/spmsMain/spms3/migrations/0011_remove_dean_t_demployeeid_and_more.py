# Generated by Django 4.1.3 on 2022-12-02 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spms3', '0010_alter_section_t_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dean_t',
            name='DEmployeeID',
        ),
        migrations.RemoveField(
            model_name='department_head_t',
            name='DepartmentID',
        ),
    ]