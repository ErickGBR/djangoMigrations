from django.contrib import admin

# Register your models here.
from .models import Flight, Airport

admin.site.register(Airport)
admin.site.register(Flight)