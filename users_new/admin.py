from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
@admin.register(CustomUser)

class CustomUserAdmin(admin.ModelAdmin):

    list_display=["id","email","first_name"]

    class Meta:
        model=CustomUser
