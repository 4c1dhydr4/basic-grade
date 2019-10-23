from django.db import models

class RoomType(models.Model):
	description = models.CharField(max_length=140, 
		blank=False, null=False,verbose_name="Descripción",
		help_text="Descripción del Tipo de Aula")
	smallCharCode = models.CharField(max_length=1,
		blank=False, null=False,verbose_name="Código",
		help_text="Código de Tipo de Aula")
	
	def __str__(self):
		return '{}'.format(self.smallCharCode)

	class Meta:
		ordering = ['smallCharCode']

class ClassRoom(models.Model):
	code = models.CharField(max_length=10, 
		blank=False, null=False,verbose_name="Código",
		help_text="Código de Aula")
	description = models.CharField(max_length=140, 
		blank=False, null=False,verbose_name="Descripción",
		help_text="Descripción de Aula")
	capacity = models.PositiveSmallIntegerField( 
		blank=False, null=False,verbose_name="Capacidad",
		help_text="Capacidad del Aula")
	roomType = models.ForeignKey(RoomType,
		blank=False, on_delete=models.CASCADE,
		help_text="Tipo de Aula",
		verbose_name="Tipo de Aula")
	
	def __str__(self):
		return '{}'.format(self.name)

	def setCode(self):
		# Setear código
		pass

	class Meta:
		ordering = ['description']