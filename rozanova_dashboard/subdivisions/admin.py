from django.contrib import admin

from subdivisions.models import Subdivision


@admin.register(Subdivision)
class SubdivisionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'type',
        'title'
    )
    fields = (
        'type',
        'title'
    )
