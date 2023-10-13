from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from . forms import RegistrationForm, EditForm
from . models import Merchant


User = get_user_model()

#M Enterprises
#LightOne Minja

class UserAdmin(UserAdmin):
    add_form = RegistrationForm
    form = EditForm
    model = User
    list_display = ['email','username','is_merchant']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('username',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser','is_merchant')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_merchant', 'is_staff', 'is_superuser')}
        ),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    
    def is_merchant(self, obj):
        return obj.is_merchant

    is_merchant.boolean = True  
    is_merchant.short_description = 'Merchant'
    
admin.site.register(User, UserAdmin)
