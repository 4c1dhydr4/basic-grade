from django.contrib import admin
from apps.courses.models import (CourseCategory, Grade,
	Turn, Section, Lesson, CourseFrequency, Course,
	CoursePlan, CoursePlanActive, CourseCategoryDetail, CourseAssignation)


class CourseCategoryAdmin(admin.ModelAdmin):
	list_display = ('code','name',)
	list_filter = tuple()
	search_fields = ('code','name',)

class GradeAdmin(admin.ModelAdmin):
	list_display = ('grade','description',)
	list_filter = ('grade',)
	search_fields = ('grade','description',)

class TurnAdmin(admin.ModelAdmin):
	list_display = ('code','name',)
	list_filter = tuple()
	search_fields = ('code','name',)

class SectionAdmin(admin.ModelAdmin):
	list_display = ('code','assign','group',)
	list_filter = tuple()
	search_fields = ('code','assign','group',)

class LessonAdmin(admin.ModelAdmin): #Falta Día
	list_display = ('day','startHour','endHour','academicHours','cronologicHour',)
	list_filter = tuple()
	search_fields = ('day','startHour','endHour','academicHours','cronologicHour',)

class CourseFrequencyAdmin(admin.ModelAdmin): #Falta Días
	list_display = ('code','name','days')
	list_filter = ('days',)
	search_fields = ('code','name','days')

class CourseAdmin(admin.ModelAdmin):
	list_display = ('code','name',)
	list_filter = tuple()
	search_fields = ('code','name',)

class CoursePlanAdmin(admin.ModelAdmin):
	list_display = ('code','name','year','institution',)
	list_filter = ('institution',)
	search_fields = ('code','name','year','institution',)

class CoursePlanActiveAdmin(admin.ModelAdmin):
	list_display = ('code','coursePlan','course','grade',)
	list_filter = ('coursePlan','course','grade',)
	search_fields = ('code','coursePlan','course','grade',)

class CourseCategoryDetailAdmin(admin.ModelAdmin):
	list_display = ('coursePlanActive','courseCategory','courseCategoryDetailHours','courseFrequency',)
	list_filter = ('coursePlanActive','courseCategory','courseFrequency',)
	search_fields = ('coursePlanActive','courseCategory','courseCategoryDetailHours','courseFrequency',)

class CourseAssignationAdmin(admin.ModelAdmin):
	list_display = ('courseCategoryDetail','teacher','lesson','classRoom','section',)
	list_filter = ('courseCategoryDetail','teacher','lesson','classRoom','section',)
	search_fields = ('courseCategoryDetail','teacher','lesson','classRoom','section',)


admin.site.register(CourseCategory, CourseCategoryAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Turn, TurnAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(CourseFrequency, CourseFrequencyAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(CoursePlan, CoursePlanAdmin)
admin.site.register(CoursePlanActive, CoursePlanActiveAdmin)
admin.site.register(CourseCategoryDetail, CourseCategoryDetailAdmin)
admin.site.register(CourseAssignation, CourseAssignationAdmin)

