# Generated by Django 5.1.1 on 2024-10-01 18:36

import builtins
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0007_alter_student_student_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': [builtins.id]},
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_id',
        ),
        migrations.AlterField(
            model_name='advisor',
            name='u_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_advisor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='advisees', to='student.advisor'),
        ),
    ]
