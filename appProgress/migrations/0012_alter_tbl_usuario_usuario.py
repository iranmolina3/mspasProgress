# Generated by Django 3.2.9 on 2022-02-09 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProgress', '0011_rename_fk_user_tbl_persona_fk_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_usuario',
            name='usuario',
            field=models.CharField(max_length=100, verbose_name='correo MSPAS'),
        ),
    ]
