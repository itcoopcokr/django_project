from django.contrib import admin

# Register your models here.
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_filter = ['title']
    list_display = ['id','title','timestamp']
    search_fields = ['title']
    class Meta:
        model = Video

admin.site.register(Video, VideoAdmin)
