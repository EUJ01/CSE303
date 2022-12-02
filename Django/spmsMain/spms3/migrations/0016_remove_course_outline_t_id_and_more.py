# Generated by Django 4.1.3 on 2022-12-02 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spms3', '0015_course_outline_t_courseprereq'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_outline_t',
            name='id',
        ),
        migrations.AddField(
            model_name='course_outline_t',
            name='CourseCode',
            field=models.CharField(default='Course', max_length=20),
        ),
        migrations.AlterField(
            model_name='course_outline_t',
            name='CourseID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
