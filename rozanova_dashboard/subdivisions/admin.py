from django.contrib import admin

from subdivisions.models import APPSubdivision


@admin.register(APPSubdivision)
class APPSubdivision(admin.ModelAdmin):
    list_display = (
        'id',
        'title'
    )
    fields = (
        'title',
    )
