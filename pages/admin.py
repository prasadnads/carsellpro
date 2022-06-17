from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style= "border-radius: 50px;" />'.format(object.photo.url))
    thumbnail.short_description = 'photo'    
    list_display = ('id', 'thumbnail', 'first_name', 'designation', 'created_date')
    list_display_links = ('id', 'thumbnail', 'first_name')
    search_fields = ('first_name', 'designation')
    list_filter = ('designation',)
    #list_per_page = 25

admin.site.register(Team, TeamAdmin)


