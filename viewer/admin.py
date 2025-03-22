from django.contrib import admin
from django.contrib.admin import ModelAdmin

from viewer.models import Movie


@admin.register(Movie)
class MovieAdmin(ModelAdmin):
    list_display = ["title","rating", "released", "description"]
    list_filter = ("rating", "genre__name", "released")
    search_fields = ["title", "description"]

    fieldsets = [
        (None, {'fields': ['title', 'created']}),
        (
            'External Information',
            {
                'fields': ['genre', 'released'],
                'description': (
                    'These fields are going to be filled with data parsed '
                    'from external databases.'
                )
            }
        ),
        (
            'User Information',
            {
                'fields': ['rating', 'description'],
                'description': 'These fields are intended to be filled in by our users.'
            }
        )
    ]
    readonly_fields = ['created']
