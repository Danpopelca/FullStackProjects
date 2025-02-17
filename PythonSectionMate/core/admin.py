from django.contrib import admin
from .models import Server, Section, ShiftAssignment

admin.site.register(Server)
admin.site.register(Section)
admin.site.register(ShiftAssignment)