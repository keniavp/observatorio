from django.contrib import admin

from Seguridad.models import ExtendUser


# Register your models here.
@admin.register(ExtendUser)
class ExtendUserAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'username', 'email', 'is_superuser', 'is_staff']
