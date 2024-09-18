from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Arrangement, Furniture


admin.site.site_header = "jonquilleBois - Administration"
    
admin.site.register(CustomUser, UserAdmin)
admin.site.register(Arrangement)
admin.site.register(Furniture)
