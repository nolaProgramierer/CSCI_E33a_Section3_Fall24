# Generated by Django 5.1.1 on 2024-10-01 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0008_alter_student_options_remove_student_student_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['id']},
        ),
        migrations.RemoveField(
            model_name='advisor',
            name='u_id',
        ),
    ]
