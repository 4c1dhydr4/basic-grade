from django.contrib import admin
from apps.demand.models import (Period,Demand,Schedule,)

class PeriodAdmin(admin.ModelAdmin):
	list_display = ('code','description',)
	list_filter = tuple()
	search_fields = ('code','description',)

class DemandAdmin(admin.ModelAdmin):
	list_display = ('institutionStar','courseCategoryDetail','turn','vacants',)
	list_filter = ('institutionStar','courseCategoryDetail','turn',)
	search_fields = ('institutionStar','courseCategoryDetail','turn','vacants',)

class ScheduleAdmin(admin.ModelAdmin):
	list_display = ('description','period','institutionStar','courseAssgnation',)
	list_filter = ('period','institutionStar','courseAssgnation',)
	search_fields = ('description','period','institutionStar','courseAssgnation',)


admin.site.register(Period, PeriodAdmin)
admin.site.register(Demand, DemandAdmin)
admin.site.register(Schedule, ScheduleAdmin)

