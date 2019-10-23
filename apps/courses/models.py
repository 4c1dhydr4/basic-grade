from django.db import models
from apps.institutions.models import Institution
from apps.teachers.models import Teacher
from apps.classRooms.models import ClassRoom


class CourseCategory(models.Model):
	code = models.CharField(max_length=10, 
		blank=False, null=False,verbose_name="Código",
		help_text="Código de Grupo")
	name = models.CharField(max_length=80, 
		blank=False, null=False,verbose_name="Nombre",
		help_text="Nombre de Categoría")
	
	def __str__(self):
		return '{}'.format(self.name)

	def setCode(self):
		# Setear código
		pass

	class Meta:
		ordering = ['name']


class Grade(models.Model):
	grade = models.PositiveSmallIntegerField( 
		blank=False, null=False,verbose_name="Ciclo",
		help_text="Ciclo")
	description = models.CharField(max_length=80, 
		blank=False, null=False,verbose_name="Descripción",
		help_text="Descripción del Ciclo")
	
	def __str__(self):
		return '{}'.format(self.description)

	class Meta:
		ordering = ['grade']


class Turn(models.Model):
	code = models.CharField(max_length=10, 
		blank=False, null=False,verbose_name="Código",
		help_text="Código de Turno")
	name = models.CharField(max_length=80, 
		blank=False, null=False,verbose_name="Nombre",
		help_text="Nombre del Turno")
	
	def __str__(self):
		return '{} {}'.format(self.code, self.name)

	def setCode(self):
		# Setear código
		pass

	class Meta:
		ordering = ['name']


class Section(models.Model):
	code = models.CharField(max_length=10, 
		blank=False, null=False,verbose_name="Código",
		help_text="Código de Sección")
	assign = models.CharField(max_length=6,
		blank=False, null=False,verbose_name="Asignación",
		help_text="Asignación")
	group = models.CharField(max_length=2,
		blank=False, null=False,verbose_name="Grupo",
		help_text="Grupo")
	
	def __str__(self):
		return '{}'.format(self.assign)

	def setCode(self):
		# Setear código
		pass

	class Meta:
		ordering = ['assign']

class Lesson(models.Model):
	startHour = models.TimeField(
		help_text="Hora de Inicio",
		verbose_name="Inicio")
	endHour = models.TimeField(
		help_text="Hora de Inicio",
		verbose_name="Inicio")
	academicHours = models.DecimalField(max_digits=3, decimal_places=2, blank=False,
		help_text="Horas Académicas)",
		verbose_name="Horas Académicas")
	cronologicHour = models.DecimalField(max_digits=3, decimal_places=2, blank=False,
		help_text="Horas Cronológicas",
		verbose_name="Horas Cronológicas")
	day = models.CharField(max_length=15,
		blank=False, null=False,verbose_name="Día",
		help_text="Día")

	def __str__(self):
		return '{} - {}'.format(self.startHour, self.endHour)

	class Meta:
		ordering = ['startHour']

class CourseFrequency(models.Model):
	code = models.CharField(max_length=10, 
		blank=False, null=False,verbose_name="Código",
		help_text="Código de Frecuencia")
	name = models.CharField(max_length=80, 
		blank=False, null=False,verbose_name="Nombre",
		help_text="Nombre de Frecuencia")
	days = models.PositiveSmallIntegerField( 
		blank=False, null=False,verbose_name="Días",
		help_text="Cantidad de Días")
	
	def __str__(self):
		return '{} {}'.format(self.code, self.name)

	def setCode(self):
		# Setear código
		pass

	class Meta:
		ordering = ['name']


class Course(models.Model):
	code = models.CharField(max_length=10, 
		blank=False, null=False,verbose_name="Código",
		help_text="Código del Curso")
	name = models.CharField(max_length=80, 
		blank=False, null=False,verbose_name="Nombre",
		help_text="Nombre del Curso")
	
	def __str__(self):
		return '{} {}'.format(self.code, self.name)

	def setCode(self):
		# Setear código
		pass

	class Meta:
		ordering = ['name']

class CoursePlan(models.Model):
	code = models.CharField(max_length=10, 
		blank=False, null=False,verbose_name="Código",
		help_text="Código del Curso")
	name = models.CharField(max_length=80, 
		blank=False, null=False,verbose_name="Nombre",
		help_text="Nombre del Curso")
	year = models.CharField(max_length=4,
		blank=False, null=False,verbose_name="Año",
		help_text="Año")
	institution = models.ForeignKey(Institution,
		blank=True, null=True, on_delete=models.CASCADE,
		help_text="Institución",
		verbose_name="Institución")

	def __str__(self):
		return '{} {}'.format(self.code, self.name)

	def setCode(self):
		# Setear código
		pass

	class Meta:
		ordering = ['name']



class CoursePlanActive(models.Model):
	code = models.CharField(max_length=10, 
		blank=False, null=False,verbose_name="Código",
		help_text="Código del Plan Activo")
	coursePlan = models.ForeignKey(CoursePlan,
		blank=False, on_delete=models.CASCADE,
		help_text="Plan Curricular",
		verbose_name="Plan Curricular")
	course = models.ForeignKey(Course,
		blank=False, on_delete=models.CASCADE,
		help_text="Curso",
		verbose_name="Curso")
	grade = models.ForeignKey(Grade,
		blank=False, on_delete=models.CASCADE,
		help_text="Ciclo",
		verbose_name="Ciclo")

	def __str__(self):
		return '{} {} {}'.format(self.code, self.course, self.coursePlan)

	def setCode(self):
		# Setear código
		pass

	class Meta:
		ordering = ['course']


class CourseCategoryDetail(models.Model):
	coursePlanActive = models.ForeignKey(CoursePlanActive,
		blank=False, on_delete=models.CASCADE,
		help_text="Plan Curricular Activo",
		verbose_name="Plan Curricular Activo")
	courseCategory = models.ForeignKey(CourseCategory,
		blank=False, on_delete=models.CASCADE,
		help_text="Categoría de Curso",
		verbose_name="Categoría de Curso")
	courseCategoryDetailHours = models.CharField(max_length=30, 
		blank=True, null=True,verbose_name="Detalle de Horas de Categoría",
		help_text="Detalle de Horas de Categoría")
	courseFrequency = models.ForeignKey(CourseFrequency,
		blank=False, on_delete=models.CASCADE,
		help_text="Frecuencia del Curso",
		verbose_name="Frecuencia del Curso")

	def __str__(self):
		return '{} - {} - {}'.format(self.coursePlanActive, self.courseCategory, self.courseFrequency)

	class Meta:
		ordering = ['coursePlanActive']


class CourseAssignation(models.Model):
	courseCategoryDetail = models.ForeignKey(CourseCategoryDetail,
		blank=False, on_delete=models.CASCADE,
		help_text="Detalle de Categoría de Curso",
		verbose_name="Detalle de Categoría de Curso")
	teacher = models.ForeignKey(Teacher,
		blank=False, on_delete=models.CASCADE,
		help_text="Profesor",
		verbose_name="Profesor")
	lesson = models.ForeignKey(Lesson,
		blank=False, on_delete=models.CASCADE,
		help_text="Clase",
		verbose_name="Clase")
	classRoom = models.ForeignKey(ClassRoom,
		blank=False, on_delete=models.CASCADE,
		help_text="Aula",
		verbose_name="Aula")
	section = models.ForeignKey(Section,
		blank=False, on_delete=models.CASCADE,
		help_text="Sección",
		verbose_name="Sección")

	def __str__(self):
		return '{} - {} - {} - {}'.format(self.teacher, self.lesson, self.classRoom, self.section)

	class Meta:
		ordering = ['section']
