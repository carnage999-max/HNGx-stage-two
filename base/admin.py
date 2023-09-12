from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ["name", "date_created"]
        

admin.site.register(CustomUser, CustomUserAdmin)