from django.db import models
from apps.institutions.models import InstitutionStar
from apps.courses.models import CourseCategoryDetail, Turn, CourseAssignation

class Period(models.Model):
	code = models.CharField(max_length=10, 
		blank=False, null=False,verbose_name="Código",
		help_text="Código de Periodo")
	description = models.CharField(max_length=80, 
		blank=False, null=False,verbose_name="Descripción",
		help_text="Descripción del Periodo")

	def __str__(self):
		return '{} {}'.format(self.code, self.description)

	class Meta:
		ordering = ['code']

class Demand(models.Model):
	institutionStar = models.ForeignKey(InstitutionStar,
		blank=True, null=True, on_delete=models.CASCADE,
		help_text="Institución Star (InstitutionStar)",
		verbose_name="Institución Star (InstitutionStar)")
	courseCategoryDetail = models.ForeignKey(CourseCategoryDetail,
		blank=True, null=True, on_delete=models.CASCADE,
		help_text="Detalle de Categoría de Curso",
		verbose_name="Detalle de Categoría de Curso")
	turn = models.ForeignKey(Turn,
		blank=True, null=True, on_delete=models.CASCADE,
		help_text="Turno",
		verbose_name="Turno")
	vacants = models.PositiveSmallIntegerField( 
		blank=False, null=False,verbose_name="Vacantes",
		help_text="Número de Vacantes")

	def __str__(self):
		return '{} Vacantes - {} - {}'.format(self.vacants,self.courseCategoryDetail, self.courseCategoryDetail)

	class Meta:
		ordering = ['institutionStar']


class Schedule(models.Model):
	description = models.CharField(max_length=80, 
		blank=False, null=False,verbose_name="Descripción",
		help_text="Descripción del Schedule")
	period = models.ForeignKey(Period,
		blank=True, null=True, on_delete=models.CASCADE,
		help_text="Periodo",
		verbose_name="Periodo")
	institutionStar = models.ForeignKey(InstitutionStar,
		blank=True, null=True, on_delete=models.CASCADE,
		help_text="Institución Star (InstitutionStar)",
		verbose_name="Institución Star (InstitutionStar)")
	courseAssgnation = models.ForeignKey(CourseAssignation,
		blank=True, null=True, on_delete=models.CASCADE,
		help_text="Asignación de Curso",
		verbose_name="Asignación de Curso")

	def __str__(self):
		return '{} - {} - {}'.format(self.period, self.courseAssgnation)

	class Meta:
		ordering = ['description']