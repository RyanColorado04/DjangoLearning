from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "age",
        "quick_description",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("age", "quick_description",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {"fields": ("age", "quick_description",)}),)


admin.site.register(CustomUser, CustomUserAdmin)