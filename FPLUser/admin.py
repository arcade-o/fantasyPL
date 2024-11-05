from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import FPLUserChangeForm,FPLUserCreationForm
from .models import FPLUser

# Register your models here.

class FPLUserAdmin(UserAdmin):
    add_form = FPLUserCreationForm
    form = FPLUserChangeForm
    model = FPLUser
    list_display = ("email","is_staff","is_active")
    list_filter = ("email","is_staff","is_active")
    fieldsets = (
        (None,{"fields": ("email","password",)}),
        ("Permissions", {"fields": ("is_staff","is_superuser","is_active","groups","user_permissions")})
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields" : (
                "email","password1","password2","is_staff","is_active",
                "groups","user_permissions", "points","balance","position",
            )}
        )
        )


search_fields = ("email")
ordering= ("email")

admin.site.register(FPLUser,FPLUserAdmin)
