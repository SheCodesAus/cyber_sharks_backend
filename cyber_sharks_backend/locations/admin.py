from django.contrib import admin
from .models import Location


class LocationAdmin(admin.ModelAdmin):
    model = Location
    list_display = ("city_name",)
    search_fields = ("city_name",)


admin.site.register(Location, LocationAdmin)
