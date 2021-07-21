from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

UserModel = get_user_model()


@admin.register(UserModel)
class AccountAdmin(UserAdmin):
    list_display = (
        'email',
        'date_joined',
        'last_login',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    search_fields = (
        'email',
    )
    readonly_fields = (
        'date_joined',
        'last_login',
    )
    ordering = (
        'date_joined',
    )
    list_filter = (
        'email',
        'date_joined',
        'last_login',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    fieldsets = (
        ('User credentials', {
            'fields': (
                'email',
                'password',
            )}),
        ('Registration and Login information', {
            'fields': (
                'date_joined',
                'last_login',
            )}),
        ('User permissions', {
            'fields': (
                'groups',
                'user_permissions',
                'is_active',
                'is_staff',
                'is_superuser',
            )}),
    )
    add_fieldsets = (
        ('User credentials', {
            'classes': (
                'wide',
            ),
            'fields': (
                'email',
                'password1',
                'password2'
            ),
        }),
    )
