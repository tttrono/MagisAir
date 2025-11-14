from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy

from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.models import User

from .forms import *
from .models import Passenger

class SignupView(CreateView):
	"""A signup view for a new user. """
	model = User
	form_class = SignupForm
	template_name = 'signup.html'
	success_url = reverse_lazy('home')
    
	def form_valid(self, form):
		""" auto-login once signed up. """
		user = form.save()
		login(self.request, user) 
		return redirect(self.success_url)
		
	def get_success_url(self):
		return redirect('passenger', args=[self.request.user.pk])
  
class PassengerInfoView(LoginRequiredMixin, UpdateView):
    """ An update view for passenger information. """
    model = Passenger
    form_class = PassengerForm
    template_name = 'passenger_information.html'
    
    def get_success_url(self):
        return reverse('home')
		

		



