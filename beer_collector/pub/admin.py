from django.contrib import admin
from beer_collector.pub.models import Pub, PubLike, PubComment


@admin.register(Pub)
class PubAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'description',
        'image',
        'longitude',
        'latitude',
        'user',
    )
    search_fields = (
        'name',
    )
    list_filter = (
        'name',
        'user',
    )
    fieldsets = (
        ('Pub info', {
            'fields': (
                'name',
                'address',
                'description',
                'image',
                'longitude',
                'latitude',
                'user',
            )}),
    )
    add_fieldsets = (
        ('Pub', {
            'classes': (
                'wide',
            ),
            'fields': (
                'name',
                'address',
                'description',
                'image',
                'longitude',
                'latitude',
                'user',
            ),
        }),
    )


@admin.register(PubLike)
class PubLikeAdmin(admin.ModelAdmin):
    list_display = (
        'pub',
        'user',
    )
    search_fields = (
        'pub',
    )
    list_filter = (
        'pub',
        'user',
    )
    fieldsets = (
        ('Pub like', {
            'fields': (
                'pub',
                'user',
            )}),
    )
    add_fieldsets = (
        ('Pub like', {
            'classes': (
                'wide',
            ),
            'fields': (
                'pub',
                'user',
            ),
        }),
    )


@admin.register(PubComment)
class PubCommentAdmin(admin.ModelAdmin):
    list_display = (
        'comment',
        'pub',
        'user',
    )
    search_fields = (
        'pub',
    )
    list_filter = (
        'pub',
        'user',
    )
    fieldsets = (
        ('Pub comments', {
            'fields': (
                'comment',
                'pub',
                'user',
            )}),
    )
    add_fieldsets = (
        ('Pub comments', {
            'classes': (
                'wide',
            ),
            'fields': (
                'comment',
                'pub',
                'user',
            ),
        }),
    )
