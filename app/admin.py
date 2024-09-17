from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Arrangement, Furniture


class AgencementAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')  # Colonnes à afficher dans la liste
    search_fields = ('title',)  # Barre de recherche sur le titre

class MobilierAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)
    
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Arrangement)
admin.site.register(Furniture)
