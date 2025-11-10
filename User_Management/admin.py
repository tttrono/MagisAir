from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Passenger

class PassengerInline(admin.StackedInline):
    """ Admin inline fields for passenger. """
    model = Passenger
    can_delete = False
    
class UserAdmin(BaseUserAdmin):
    """ Admin panel for passenger. """
    inlines = [PassengerInline,]
    
#admin.site.register(Passenger)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
