# Generated by Django 4.1.3 on 2022-12-07 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CMAS', '0002_alter_clo_courseid_alter_clo_ploid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clo',
            name='courseid',
            field=models.ForeignKey(db_column='CoID', on_delete=django.db.models.deletion.DO_NOTHING, to='CMAS.courseoutline'),
        ),
    ]
