from django.contrib import admin
from . models import coffeeModel

# Register your models here.

class coffeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

admin.site.register(coffeeModel, coffeeAdmin)