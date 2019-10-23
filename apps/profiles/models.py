from django.db import models
from django.utils import timezone

class ProfileType(models.Model):
	name = models.CharField(max_length=50, 
		blank=False, null=False,verbose_name="Nombre del TIpo de Perfil",
		help_text="Nombre")
	description = models.CharField(max_length=100, 
		blank=False, null=False,verbose_name="Descripción",
		help_text="Descripción")
	smallChar = models.CharField(max_length=1, 
		blank=False, null=False,verbose_name="Small Code",
		help_text="Small Code")

	def __str__(self):
		return '{}'.format(self.name)

	class Meta:
		ordering = ['name']


class Profile(models.Model):
	names = models.CharField(max_length=100, 
		blank=False, null=False,verbose_name="Nombres",
		help_text="Nombres")
	last_name_p = models.CharField(max_length=100, 
		blank=False, null=False,verbose_name="Apellido Paterno",
		help_text="Apellido Paterno")
	last_name_m = models.CharField(max_length=100, 
		blank=False, null=False,verbose_name="Apellido Materno",
		help_text="Apellido Materno")
	mobile_number = models.CharField(max_length=20, blank=True,
		help_text="Número de Teléfono Celular",
		verbose_name="Celular")
	phone = models.CharField(max_length=20, blank=True,
		help_text="Número de Teléfono Fijo o de Oficina",
		verbose_name="Teléfono")
	born_date = models.DateField(blank=True, null=True,
		help_text="Fecha de Nacimiento",
		verbose_name="Nacimiento")
	email = models.EmailField(max_length=40, blank=True,
		help_text="Correo Electrónico",
		verbose_name="Email")
	registerDate = models.DateField(default=timezone.now,
		help_text="Fecha de Registro",
		verbose_name="Fecha de Registro")
	dni = models.CharField(max_length=8, blank=True,
		help_text="Número de DNI",
		verbose_name="DNI")
	profileType = models.ForeignKey(ProfileType,
		blank=False, on_delete=models.CASCADE,
		help_text="Tipo de Perfil",
		verbose_name="Tipo de Perfil")

	def __str__(self):
		return '{}'.format(self.names)

	class Meta:
		ordering = ['names']

