from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Text_and_video)
class TasksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'original_text_url', 'original_video_url')
    list_filter = ('title', )
    list_per_page = 20


@admin.register(Persons)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'grade', 'age')
    list_filter = ('grade', 'age')
    search_fields = ('name',)
    list_per_page = 30

    readonly_fields = ('password',)

