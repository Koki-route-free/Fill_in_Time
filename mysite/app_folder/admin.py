from django.contrib import admin
# Register your models here.

# models.pyで指定したクラス名
from .models import UserDB

from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import SampleDB

# admin.site.register(UserDB)
@admin.register(UserDB)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal Info',), {'fields': ('email',)}),
        (_('Permissions',), {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
        (_('Password',), {'fields': ('password_changed', 'password_changed_date',)}),
        (_('Important Dates',), {'fields': ('last_login', 'date_joined',)}),
    )

    list_display = ('username', 'email', 'is_active',)


admin.site.register(SampleDB)