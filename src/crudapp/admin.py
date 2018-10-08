from django.contrib import admin

# Register your models here.
from .models import Profile


class AdminProfile(admin.ModelAdmin):
	list_display = ['name', 'email', 'mobile', 'address']


admin.site.register(Profile, AdminProfile)