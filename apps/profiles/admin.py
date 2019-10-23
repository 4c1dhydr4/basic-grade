from django.contrib import admin
from apps.profiles.models import (ProfileType,Profile)

class ProfileTypeAdmin(admin.ModelAdmin):
	list_display = ('name','description','smallChar',)
	list_filter = ('smallChar',)
	search_fields = ('name','description','smallChar',)


class ProfileAdmin(admin.ModelAdmin):
	list_display = ('names','last_name_p','last_name_m','mobile_number','born_date','email','dni','profileType',)
	list_filter = ('profileType',)
	search_fields = ('names','last_name_p','last_name_m','mobile_number','phone','email','dni',)


admin.site.register(ProfileType, ProfileTypeAdmin)
admin.site.register(Profile, ProfileAdmin)

