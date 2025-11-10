from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import *

class SignupForm(UserCreationForm):
    class Meta: 
        model = User
        fields = ['username', 'email']

class PassengerUpdateForm(ModelForm):
    """A form for updating passenger information. """
    class Meta:
        model = Passenger
        exclude=['user']
