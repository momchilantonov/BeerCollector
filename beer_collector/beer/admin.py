from django.contrib import admin
from beer_collector.beer.models import BeerStyle, Beer, BeerLike


@admin.register(BeerStyle)
class BeerStyleAdmin(admin.ModelAdmin):
    list_display = (
        'type',
    )
    search_fields = (
        'type',
    )
    list_filter = (
        'type',
    )
    fieldsets = (
        ('Beer style', {
            'fields': (
                'type',
            )}),
    )
    add_fieldsets = (
        ('Beer style', {
            'classes': (
                'wide',
            ),
            'fields': (
                'type',
            ),
        }),
    )


@admin.register(Beer)
class BeerAdmin(admin.ModelAdmin):
    list_display = (
        'label',
        'type',
        'description',
        'image',
        'user',
    )
    search_fields = (
        'label',
        'type',
    )
    list_filter = (
        'label',
        'type',
        'description',
        'image',
        'user',
    )
    fieldsets = (
        ('Beer info', {
            'fields': (
                'label',
                'type',
                'description',
                'image',
                'user',
            )}),
    )
    add_fieldsets = (
        ('Beer', {
            'classes': (
                'wide',
            ),
            'fields': (
                'label',
                'type',
                'description',
                'image',
                'user',
            ),
        }),
    )


@admin.register(BeerLike)
class BeerLikeAdmin(admin.ModelAdmin):
    list_display = (
        'beer',
        'user',
    )
    search_fields = (
        'beer',
    )
    list_filter = (
        'beer',
        'user',
    )
    fieldsets = (
        ('Beer like', {
            'fields': (
                'beer',
                'user',
            )}),
    )
    add_fieldsets = (
        ('Beer like', {
            'classes': (
                'wide',
            ),
            'fields': (
                'beer',
                'user',
            ),
        }),
    )
