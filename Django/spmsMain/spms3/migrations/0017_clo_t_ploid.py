# Generated by Django 4.1.3 on 2022-12-03 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spms3', '0016_remove_course_outline_t_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='clo_t',
            name='PLOID',
            field=models.ForeignKey(default='Null', on_delete=django.db.models.deletion.CASCADE, to='spms3.plo_t'),
        ),
    ]