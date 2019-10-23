from django.contrib import admin
from apps.classRooms.models import (RoomType, ClassRoom)

class RoomTypeAdmin(admin.ModelAdmin):
	list_display = ('description','smallCharCode',)
	list_filter = tuple()
	search_fields = ('description','smallCharCode',)

class ClassRoomAdmin(admin.ModelAdmin):
	list_display = ('code','description','capacity','roomType',)
	list_filter = ('roomType',)
	search_fields = ('code','description','capacity','roomType',)


admin.site.register(RoomType, RoomTypeAdmin)
admin.site.register(ClassRoom, ClassRoomAdmin)