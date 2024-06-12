from django.contrib import admin

# Register your models here.
from .models import Flight, Airport, passenger

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(passenger)