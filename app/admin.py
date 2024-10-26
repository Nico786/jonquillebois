from django.contrib import admin, messages
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Arrangement, Furniture
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from adminsortable2.admin import SortableAdminMixin
from .forms import StaffUserUpdateForm

admin.site.site_header = "jonquilleBois - Administration"

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'email', 'phone', 'address')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'phone', 'address'),
        }),
    )

    list_display = ('username', 'email', 'first_name', 'is_staff', 'phone', 'address')
    
    def get_form(self, request, obj=None, **kwargs):
        if obj is not None and request.user.is_staff and not request.user.is_superuser:
            if request.user == obj:
                self.form = StaffUserUpdateForm
        return super().get_form(request, obj, **kwargs)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_staff and not request.user.is_superuser:
            # l'utilisateur is_staff ne peut voir que son propre compte
            return qs.filter(id=request.user.id)
        return qs

class RealisationAdmin(SortableAdminMixin,admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        try:
            obj.clean()
        except ValidationError as e:
            self.message_user(request, str(e), level=messages.ERROR)
            return
        super().save_model(request, obj, form, change)
    list_display = ('title', 'description', 'main_picture', 'position')

@admin.register(Arrangement)
class ArrangementAdmin(RealisationAdmin):
    pass

@admin.register(Furniture)
class FurnitureAdmin(RealisationAdmin):
    pass
