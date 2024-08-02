from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

# Register your models here.


class AccountAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('email', 'password')
        }),
        ('Personal Information', {
            "fields": ('first_name', 'last_name')
        }),
        ("Permissions", {
            'fields': ('is_active', 'is_staff', 'is_superuser')
        }),

    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2')}
         ),
    )
    list_display = ['email', 'username', 'is_active', 'is_superuser']
    list_filter = ['is_active', 'is_superuser']
    search_fields = ('email', 'username')
    ordering = ['email']
    filter_horizontal = []


admin.site.register(Account, AccountAdmin)
