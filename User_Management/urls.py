from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('<int:pk>/', PassengerUpdateView.as_view(), name='update'),
]

app_name = 'User_Management'
