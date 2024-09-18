from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Arrangement, Furniture
from django.core.exceptions import ValidationError

admin.site.site_header = "jonquilleBois - Administration"

admin.site.register(CustomUser, UserAdmin)

class RealisationAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.clean()
        except ValidationError as e:
            self.message_user(request, str(e), level=messages.ERROR)
            return
        super().save_model(request, obj, form, change)

@admin.register(Arrangement)
class ArrangementAdmin(RealisationAdmin):
    pass

@admin.register(Furniture)
class FurnitureAdmin(RealisationAdmin):
    pass