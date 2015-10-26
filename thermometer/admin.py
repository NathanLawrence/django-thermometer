from django.contrib import admin

from .models import Therm

class ThermAdmin(admin.ModelAdmin):
	list_display =  ['name','heading','fundGoal','fundCurrent']

admin.site.register(Therm,ThermAdmin)