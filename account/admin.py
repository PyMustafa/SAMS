from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from SAMS.models import Student, Professor

from account.models import Account



class AccountAdmin(UserAdmin):
    list_display = ('email', 'data_Joined', 'last_login', 'is_admin', 'is_staff')
    search_fields = ('email',)
    readonly_fields = ( 'data_Joined', 'last_login')
    ordering = ('email',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )



admin.site.register(Account, AccountAdmin)

admin.site.register(Student)
admin.site.register(Professor)