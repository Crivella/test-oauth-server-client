from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from . import models as m

# Register your models here.


class UserAdmin(BaseUserAdmin):
    # list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser')
    # list_filter = ('is_staff', 'is_superuser')
    # search_fields = ('username', 'email', 'first_name', 'last_name')
    pass

admin.site.register(m.User, UserAdmin)