# Generated by Django 4.1.3 on 2022-12-07 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CMAS', '0003_alter_clo_courseid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='courseid',
        ),
    ]
