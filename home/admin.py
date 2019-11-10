from django.contrib import admin
from home.models import *

# Register your models here.
admin.site.register(Otpt)

@admin.register(user)
class userAdmin(admin.ModelAdmin):
    pass

@admin.register(media)
class mediaAdmin(admin.ModelAdmin):
    pass

@admin.register(order)
class orderAdmin(admin.ModelAdmin):
    pass

@admin.register(vehicle)
class vehicleAdmin(admin.ModelAdmin):
    pass

@admin.register(select)
class selectAdmin(admin.ModelAdmin):
    pass

# from django.contrib import admin
# from home.models import *
# # Register your models here.
# admin.site.register(user)
# admin.site.register(vehicle)
# admin.site.register(courier)