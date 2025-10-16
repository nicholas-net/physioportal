from django.contrib import admin

from .models import Exercise, Patient, Program

admin.site.register(Exercise)
admin.site.register(Patient)
admin.site.register(Program)


