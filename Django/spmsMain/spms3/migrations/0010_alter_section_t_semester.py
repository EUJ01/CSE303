# Generated by Django 4.1.3 on 2022-12-02 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spms3', '0009_remove_faculty_t_femployeeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section_t',
            name='Semester',
            field=models.CharField(max_length=50),
        ),
    ]