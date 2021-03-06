# Generated by Django 3.2.9 on 2021-11-22 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appProgress', '0006_tbl_sub_asignatura'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_nota_sub_asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(null=True, verbose_name='descripcion')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='fecha creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='fecha modificacion')),
                ('fk_asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProgress.tbl_sub_asignatura')),
            ],
        ),
        migrations.CreateModel(
            name='tbl_nota_asignatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(null=True, verbose_name='descripcion')),
                ('fecha_creacion', models.DateField(auto_now_add=True, verbose_name='fecha creacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='fecha modificacion')),
                ('fk_asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProgress.tbl_asignatura')),
            ],
        ),
    ]
