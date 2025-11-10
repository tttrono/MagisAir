from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy

from django.views.generic import TemplateView

from . import templates

class HomeView(TemplateView):
    template_name = 'home.html'
    

