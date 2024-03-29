# Generated by Django 2.1.5 on 2019-02-16 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('institutions', '0001_initial'),
        ('courses', '0002_auto_20190216_1948'),
    ]

    operations = [
        migrations.CreateModel(
            name='Demand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vacants', models.PositiveSmallIntegerField(help_text='Número de Vacantes', verbose_name='Vacantes')),
                ('courseCategoryDetail', models.ForeignKey(blank=True, help_text='Detalle de Categoría de Curso', null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.CourseCategoryDetail', verbose_name='Detalle de Categoría de Curso')),
                ('institutionStar', models.ForeignKey(blank=True, help_text='Institución Star (InstitutionStar)', null=True, on_delete=django.db.models.deletion.CASCADE, to='institutions.InstitutionStar', verbose_name='Institución Star (InstitutionStar)')),
                ('turn', models.ForeignKey(blank=True, help_text='Turno', null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Turn', verbose_name='Turno')),
            ],
            options={
                'ordering': ['institutionStar'],
            },
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(help_text='Código de Periodo', max_length=10, verbose_name='Código')),
                ('description', models.CharField(help_text='Descripción del Periodo', max_length=80, verbose_name='Descripción')),
            ],
            options={
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(help_text='Descripción del Schedule', max_length=80, verbose_name='Descripción')),
                ('courseAssgnation', models.ForeignKey(blank=True, help_text='Asignación de Curso', null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.CourseAssignation', verbose_name='Asignación de Curso')),
                ('institutionStar', models.ForeignKey(blank=True, help_text='Institución Star (InstitutionStar)', null=True, on_delete=django.db.models.deletion.CASCADE, to='institutions.InstitutionStar', verbose_name='Institución Star (InstitutionStar)')),
                ('period', models.ForeignKey(blank=True, help_text='Periodo', null=True, on_delete=django.db.models.deletion.CASCADE, to='demand.Period', verbose_name='Periodo')),
            ],
            options={
                'ordering': ['description'],
            },
        ),
    ]
