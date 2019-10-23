from django.db import models
from apps.profiles.models import Profile
from apps.institutions.models import (Subsidiary, Faculty)

class TeacherType(models.Model):
	name = models.CharField(max_length=80, 
		blank=False, null=False,verbose_name="Nombre",
		help_text="Tipo de Docente")
	description = models.CharField(max_length=100, 
		blank=False, null=False,verbose_name="Descripción",
		help_text="Descripción del Tipo de Docente")

	def __str__(self):
		return '{}'.format(self.name)

	class Meta:
		ordering = ['name']

class TeacherSalary(models.Model):
	name = models.CharField(max_length=80, 
		blank=False, null=False,verbose_name="Nombre",
		help_text="Nombre del Salario")
	value = models.DecimalField(max_digits=8, decimal_places=2, blank=False,
		help_text="Salario",
		verbose_name="Salario")
	teacherType = models.ForeignKey(TeacherType,
		blank=False, on_delete=models.CASCADE,
		help_text="Tipo de Docente",
		verbose_name="Tipo de Docente")
	subsidiary = models.ForeignKey(Subsidiary,
		blank=False, on_delete=models.CASCADE,
		help_text="Sede",
		verbose_name="Sede")

	def __str__(self):
		return '{}'.format(self.name)

	class Meta:
		ordering = ['name']


class Teacher(models.Model):
	code = models.CharField(max_length=10, 
		blank=False, null=False,verbose_name="Código",
		help_text="Código del Curso")
	originSubsidiary = models.ForeignKey(Subsidiary,
		blank=False, on_delete=models.CASCADE,
		help_text="Sede de Origen",
		verbose_name="Sede de Origen")
	faculty = models.ForeignKey(Faculty,
		blank=False, on_delete=models.CASCADE,
		help_text="Escuela",
		verbose_name="Escuela")
	teacherType = models.ForeignKey(TeacherType,
		blank=False, on_delete=models.CASCADE,
		help_text="Tipo de Profesor",
		verbose_name="Tipo de Profesor")
	profile = models.ForeignKey(Profile,
		blank=False, on_delete=models.CASCADE,
		help_text="Perfil Enlazado",
		verbose_name="Perfil")

	def __str__(self):
		return '{}'.format(self.profile)

	def setCode(self):
		# Setear código
		pass

	class Meta:
		ordering = ['profile']