from django.contrib import admin

from .models import Photo
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title','user','timestamp')

admin.site.register(Photo, PhotoAdmin)
