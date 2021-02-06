from django.contrib import admin
from .models import Curiosities

class CuriositiesAdmin(admin.ModelAdmin):
    fields = [
        "author_name",
        "published_date",
        "curiosity"
    ]

# Register your models here.
admin.site.register(Curiosities,CuriositiesAdmin)