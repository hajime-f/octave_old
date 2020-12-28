from .models import User
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

# class UserModelAdmin(admin.ModelAdmin):
#     #ordering('-created_at',)
#     #readonly_fields = ('id', 'uuid', 'created_at',)

#     def change_view(self, request, object_id, form_url='', extra_context=None):
#         self.readonly_fields = ('id', 'uuid', 'created_at',)
#         return self.changeform_view(request, object_id, form_url, extra_context)

#     def add_view(self, request, form_url='', extra_context=None):
#         self.readonly_fields = ()
#         return self.changeform_view(request, None, form_url, extra_context)    

@admin.register(User)
class AdminUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('last_name', 'first_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'is_staff')
    search_fields = ('username', 'email')
    filter_horizontal = ('groups', 'user_permissions')
