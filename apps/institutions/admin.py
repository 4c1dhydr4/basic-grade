from django.contrib import admin
from apps.institutions.models import (Institution,Modality,
	Subsidiary,Faculty,Career, InstitutionStar)


class InstitutionAdmin(admin.ModelAdmin):
	list_display = ('code','name',)
	list_filter = tuple()
	search_fields = ('code','name',)

class SubsidiaryAdmin(admin.ModelAdmin):
	list_display = ('code','institution','description','shortDescription',)
	list_filter = ('institution',)
	search_fields = ('code','institution__name','description','shortDescription',)

class CareerAdmin(admin.ModelAdmin):
	list_display = ('code','name',)
	list_filter = tuple()
	search_fields = ('code','name',)

class ModalityAdmin(admin.ModelAdmin):
	list_display = ('code','description','shortDescription')
	list_filter = tuple()
	search_fields = ('code','description','shortDescription')

class FacultyAdmin(admin.ModelAdmin):
	list_display = ('code','name',)
	list_filter = tuple()
	search_fields = ('code','name',)

class InstitutionStarAdmin(admin.ModelAdmin):
	list_display = ('subsidiary','faculty','career','modality',)
	list_filter = ('subsidiary','faculty','career','modality',)
	search_fields = ('subsidiary__description','faculty__name','career__name','modality__description',)


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(Subsidiary, SubsidiaryAdmin)
admin.site.register(Career, CareerAdmin)
admin.site.register(Modality, ModalityAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(InstitutionStar, InstitutionStarAdmin)

