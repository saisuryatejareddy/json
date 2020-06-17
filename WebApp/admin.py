from django.contrib import admin
from WebApp.models import Json
# Register your models here.
class JAdmin(admin.ModelAdmin):
    list_display = ['JsonFile']
admin.site.register(Json,JAdmin)