from django.contrib import admin
from cars.models import Car
from cars.models import Brand

class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'factory_year', 'model_year', 'value')
    search_fields = ('brand', 'model')
    


class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name', 'id')
    
admin.site.register(Brand, BrandAdmin)
admin.site.register(Car, CarAdmin)