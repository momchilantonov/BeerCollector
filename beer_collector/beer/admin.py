from django.contrib import admin
from beer_collector.beer.models import BeerStyle, Beer, BeerLike, BeerStyleLike, BeerStyleComment, BeerComment


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


@admin.register(BeerStyleLike)
class BeerStyleLikeAdmin(admin.ModelAdmin):
    list_display = (
        'beer_style',
        'user',
    )
    search_fields = (
        'beer_style',
    )
    list_filter = (
        'beer_style',
        'user',
    )
    fieldsets = (
        ('Beer style like', {
            'fields': (
                'beer_style',
                'user',
            )}),
    )
    add_fieldsets = (
        ('Beer style like', {
            'classes': (
                'wide',
            ),
            'fields': (
                'beer_style',
                'user',
            ),
        }),
    )


@admin.register(BeerStyleComment)
class BeerStyleCommentAdmin(admin.ModelAdmin):
    list_display = (
        'comment',
        'beer_style',
        'user',
    )
    search_fields = (
        'beer_style',
    )
    list_filter = (
        'beer_style',
        'user',
    )
    fieldsets = (
        ('Beer style comments', {
            'fields': (
                'comment',
                'beer_style',
                'user',
            )}),
    )
    add_fieldsets = (
        ('Beer style comments', {
            'classes': (
                'wide',
            ),
            'fields': (
                'comment',
                'beer_style',
                'user',
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


@admin.register(BeerComment)
class BeerCommentAdmin(admin.ModelAdmin):
    list_display = (
        'comment',
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
        ('Beer comments', {
            'fields': (
                'comment',
                'beer',
                'user',
            )}),
    )
    add_fieldsets = (
        ('Beer comments', {
            'classes': (
                'wide',
            ),
            'fields': (
                'comment',
                'beer',
                'user',
            ),
        }),
    )
