from django.contrib import admin
from .models import Category, City, Tip, Restaurant, Payment, Establishment

# Register your models here.
# Registrar modelos al administrador 

admin.site.register(Category)
admin.site.register(City)
admin.site.register(Tip)
admin.site.register(Restaurant)
admin.site.register(Payment)
admin.site.register(Establishment)
