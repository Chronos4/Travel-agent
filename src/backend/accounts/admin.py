from django.contrib import admin
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from .forms import UserAdminChangeForm, UserAdminCreateForm
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.
user = get_user_model()


class UserAdmin(BaseUserAdmin):
    list_display = ['__str__', 'slug', 'active', 'staff', 'admin', 'timestamp']
    ordering = ('-timestamp',)
    list_filter = ('staff', 'admin', 'active',)
    search_fields = ['email', 'slug', 'hobbies', 'description']
    form = UserAdminChangeForm
    add_form = UserAdminCreateForm
    readonly_fields = ('timestamp', 'updated')
    fieldsets = [
        ('Username email', {
         'fields': ('email', 'password', 'timestamp', 'updated')}),
        ('Personal_info', {
         'fields': ('first_name', 'last_name', 'age', 'slug')}),
        ('Other Info', {'fields': ('hobbies',
                                   'description', 'places_been', 'places_to')}),
        ('Permissions', {'fields': ('admin', 'staff', 'active',)})
    ]

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'last_name', 'first_name', 'age', 'password', 'password2')}
         ),
    )
    filter_horizontal = ()


admin.site.register(user, UserAdmin)
admin.site.unregister(Group)
