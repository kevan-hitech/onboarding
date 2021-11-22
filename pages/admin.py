from django.contrib import admin

from .models import Checklist, Sheet

admin.site.register(Sheet)
admin.site.register(Checklist)