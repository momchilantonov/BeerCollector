from django.contrib import admin
from beer_collector.collector_profile.models import CollectorProfile


@admin.register(CollectorProfile)
class CollectorProfileAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    # def has_delete_permission(self, request, obj=None):
    #     return False

    list_display = (
        'username',
        'first_name',
        'last_name',
        'about',
        'image',
        'is_complete',
        'user',
    )
    search_fields = (
        'username',
        'first_name',
        'last_name',
    )
    list_filter = (
        'username',
        'first_name',
        'last_name',
        'about',
        'image',
        'is_complete',
        'user',
    )
    fieldsets = (
        ('User info', {
            'fields': (
                'username',
                'first_name',
                'last_name',
                'about',
                'image',
                'is_complete',
                'user',
            )}),
    )
