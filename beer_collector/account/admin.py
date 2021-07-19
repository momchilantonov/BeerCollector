from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

UserModel = get_user_model()


@admin.register(UserModel)
class AccountAdmin(UserAdmin):
    list_display = (
        'email',
        'username',
        'first_name',
        'last_name',
        'registration_date',
        'last_login',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    search_fields = (
        'email',
        'username',
    )
    readonly_fields = (
        'registration_date',
        'last_login',
    )
    ordering = (
        'registration_date',
    )
    list_filter = (
        'email',
        'username',
        'first_name',
        'last_name',
        'registration_date',
        'last_login',
        'is_active',
        'is_staff',
        'is_superuser',
    )
    fieldsets = (
        ('User credentials', {
            'fields': (
                'email',
                'username',
                'first_name',
                'last_name',
                'password',
            )}),
        ('Registration and Login information', {
            'fields': (
                'registration_date',
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
                'username',
                'first_name',
                'last_name',
                'password1',
                'password2'
            ),
        }),
    )
