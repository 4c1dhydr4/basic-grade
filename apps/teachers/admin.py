from django.contrib import admin
from apps.teachers.models import (TeacherType,TeacherSalary,Teacher)

class TeacherTypeAdmin(admin.ModelAdmin):
	list_display = ('name','description',)
	list_filter = tuple()
	search_fields = ('name','description',)

class TeacherSalaryAdmin(admin.ModelAdmin):
	list_display = ('name','subsidiary','teacherType','value')
	list_filter = ('subsidiary',)
	search_fields = ('name','subsidiary','teacherType','value')

class TeacherAdmin(admin.ModelAdmin):
	list_display = ('code','profile','originSubsidiary','faculty','teacherType',)
	list_filter = ('profile','originSubsidiary','faculty','teacherType',)
	search_fields = ('code','profile__names','profile__last_name_p','profile__last_name_m')

admin.site.register(TeacherType, TeacherTypeAdmin)
admin.site.register(TeacherSalary, TeacherSalaryAdmin)
admin.site.register(Teacher, TeacherAdmin)
