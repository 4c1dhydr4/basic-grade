from django.db import models

class Institution(models.Model):
	code = models.CharField(max_length=10, 
		blank=False, null=False,verbose_name="Código",
		help_text="Código de Institución")
	name = models.CharField(max_length=80, 
		blank=False, null=False,verbose_name="Nombre",
		help_text="Nombre de Institución")

	def __str__(self):
		return '{}'.format(self.name)

	def setCode(self):
		# Setear código
		pass

	class Meta:
		ordering = ['name']


class Subsidiary(models.Model):
	code = models.CharField(max_length=10, 
		blank=False, null=False,verbose_name="Código",
		help_text="Código de Sede")
	description = models.CharField(max_length=100, 
		blank=False, null=False,verbose_name="Descripción",
		help_text="Descripción")
	shortDescription = models.CharField(max_length=25, 
		blank=False, null=False,verbose_name="Descripción Corta",
		help_text="Descripción Corta")
	institution = models.ForeignKey(Institution,
		blank=False, on_delete=models.CASCADE,
		help_text="Institución",
		verbose_name="Institución")


	def __str__(self):
		return '{}'.format(self.shortDescription)

	def setCode(self):
		# Setear código
		pass

	class Meta:
		ordering = ['shortDescription']


class Career(models.Model):
	code = models.CharField(max_length=10, 
		blank=False, null=False,verbose_name="Código Carrera",
		help_text="Código de Carrera")
	name = models.CharField(max_length=100, 
		blank=False, null=False,verbose_name="Nombre Carrera",
		help_text="Nombre de la Carrera")

	def __str__(self):
		return '{}'.format(self.name)

	def setCode(self):
		# Setear código
		pass

	class Meta:
		ordering = ['name']


class Modality(models.Model):
	code = models.CharField(max_length=10, 
		blank=False, null=False,verbose_name="Código Modalidad",
		help_text="Código de Modalidad")
	description = models.CharField(max_length=100, 
		blank=False, null=False,verbose_name="Descripción",
		help_text="Descripción de la Modalidad")
	shortDescription = models.CharField(max_length=100, 
		blank=False, null=False,verbose_name="Descripción Corta",
		help_text="Descripción corta de la Modalidad")

	def __str__(self):
		return '{}'.format(self.description)

	def setCode(self):
		# Setear código
		pass

	class Meta:
		ordering = ['description']


class Faculty(models.Model):
	code = models.CharField(max_length=10, 
		blank=False, null=False,verbose_name="Código",
		help_text="Código de Escuela")
	name = models.CharField(max_length=80, 
		blank=False, null=False,verbose_name="Nombre",
		help_text="Nombre de Escuela")

	def __str__(self):
		return '{}'.format(self.name)

	def setCode(self):
		# Setear código
		pass

	class Meta:
		ordering = ['name']


class InstitutionStar(models.Model):
	subsidiary = models.ForeignKey(Subsidiary,
		blank=False, on_delete=models.CASCADE,
		help_text="Filial",
		verbose_name="Filial")
	faculty = models.ForeignKey(Faculty,
		blank=False, on_delete=models.CASCADE,
		help_text="Facultad",
		verbose_name="Facultad")
	career = models.ForeignKey(Career,
		blank=False, on_delete=models.CASCADE,
		help_text="Carrera",
		verbose_name="Carrera")
	modality = models.ForeignKey(Modality,
		blank=False, on_delete=models.CASCADE,
		help_text="Modalidad",
		verbose_name="Modalidad")

	def __str__(self):
		return '{} - {} - {} - {}'.format(self.subsidiary,self.faculty,self.career,self.modality)

	class Meta:
		ordering = ['career']
